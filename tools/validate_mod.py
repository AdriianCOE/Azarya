#!/usr/bin/env python3
"""Read-only sanity checks for the Azaryafantasia mod tree.

Run from anywhere: `python tools/validate_mod.py`. Only prints findings,
never modifies any file.
"""
import re
import sys
from pathlib import Path
from collections import defaultdict

MOD_ROOT = Path(__file__).resolve().parent.parent


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def section(title: str):
    print(f"\n=== {title} ===")


# ---------------------------------------------------------------------------
# 1/2. country_tags <-> countries files
# ---------------------------------------------------------------------------
def check_country_tags():
    tags_dir = MOD_ROOT / "common" / "country_tags"
    countries_dir = MOD_ROOT / "common" / "countries"

    tag_to_file = {}  # TAG -> relative path string, e.g. "countries/Foo.txt"
    for f in sorted(tags_dir.glob("*.txt")):
        text = read_text(f)
        for m in re.finditer(r'^\s*([A-Z0-9]{3})\s*=\s*"([^"]+)"', text, re.M):
            tag_to_file[m.group(1)] = m.group(2)

    section("Tags sem country file")
    missing = 0
    for tag, rel_path in sorted(tag_to_file.items()):
        target = MOD_ROOT / "common" / rel_path
        if not target.is_file():
            print(f"  {tag} -> common/{rel_path} (NAO EXISTE)")
            missing += 1
    print(f"Total: {missing} tag(s) apontando para arquivo inexistente, de {len(tag_to_file)} tags.")

    section("Country files sem tag")
    referenced = {Path(p).name for p in tag_to_file.values()}
    orphans = 0
    for f in sorted(countries_dir.glob("*.txt")):
        if f.name not in referenced:
            print(f"  common/countries/{f.name} (nenhuma tag aponta para ele)")
            orphans += 1
    print(f"Total: {orphans} arquivo(s) de countries sem tag.")

    return tag_to_file


# ---------------------------------------------------------------------------
# 3. history/countries files sem tag conhecida
# ---------------------------------------------------------------------------
def check_history_countries(known_tags):
    section("History files sem tag")
    hdir = MOD_ROOT / "history" / "countries"
    bad = 0
    for f in sorted(hdir.glob("*.txt")):
        m = re.match(r"^([A-Z0-9]{2,3})", f.stem)
        tag = m.group(1) if m else None
        if not tag or tag not in known_tags:
            print(f"  history/countries/{f.name} (prefixo de tag '{tag}' nao reconhecido)")
            bad += 1
    print(f"Total: {bad} arquivo(s) de history/countries com tag nao reconhecida.")


# ---------------------------------------------------------------------------
# 4. Localisation duplicada
# ---------------------------------------------------------------------------
def check_localisation_duplicates():
    section("Localisation duplicada")
    ldir = MOD_ROOT / "localisation"
    total = 0
    for f in sorted(ldir.rglob("*.yml")):
        text = read_text(f)
        seen = {}
        for lineno, line in enumerate(text.splitlines(), start=1):
            m = re.match(r"^\s*([A-Za-z0-9_.\-]+):\d*\s", line)
            if not m:
                continue
            key = m.group(1)
            if key in seen:
                print(f"  {f.relative_to(MOD_ROOT)}: chave '{key}' duplicada (linhas {seen[key]} e {lineno})")
                total += 1
            else:
                seen[key] = lineno
    print(f"Total: {total} chave(s) duplicada(s).")


# ---------------------------------------------------------------------------
# 5. Focus IDs duplicados
# ---------------------------------------------------------------------------
def check_focus_id_duplicates():
    section("Focus IDs duplicados")
    fdir = MOD_ROOT / "common" / "national_focus"
    seen = {}
    dup = 0
    for f in sorted(fdir.glob("*.txt")):
        text = read_text(f)
        for m in re.finditer(r"^\s*id\s*=\s*([A-Za-z0-9_.\-]+)", text, re.M):
            fid = m.group(1)
            if fid in seen and seen[fid] != f.name:
                print(f"  id '{fid}' aparece em {seen[fid]} e em {f.name}")
                dup += 1
            else:
                seen[fid] = f.name
    print(f"Total: {dup} id(s) de focus duplicado(s) entre arquivos ({len(seen)} ids unicos vistos).")


# ---------------------------------------------------------------------------
# 6. Event IDs duplicados
# ---------------------------------------------------------------------------
def check_event_id_duplicates():
    section("Event IDs duplicados")
    edir = MOD_ROOT / "events"
    seen = {}
    dup = 0
    for f in sorted(edir.glob("*.txt")):
        text = read_text(f)
        for m in re.finditer(r"^\s*id\s*=\s*([A-Za-z0-9_]+\.\d+)", text, re.M):
            eid = m.group(1)
            if eid in seen and seen[eid] != f.name:
                print(f"  id '{eid}' aparece em {seen[eid]} e em {f.name}")
                dup += 1
            else:
                seen[eid] = f.name
    print(f"Total: {dup} id(s) de evento duplicado(s) entre arquivos ({len(seen)} ids unicos vistos).")


# ---------------------------------------------------------------------------
# 7. GFX referenciado mas nao definido (best-effort)
# ---------------------------------------------------------------------------
def check_gfx_references():
    section("Referencias GFX possivelmente inexistentes (best-effort)")
    defined = set()
    for f in MOD_ROOT.rglob("*.gfx"):
        text = read_text(f)
        defined.update(re.findall(r'name\s*=\s*"(GFX_[A-Za-z0-9_]+)"', text))

    used = set()
    search_dirs = [MOD_ROOT / "events", MOD_ROOT / "common" / "national_focus", MOD_ROOT / "interface"]
    usage_locations = defaultdict(list)
    for d in search_dirs:
        if not d.exists():
            continue
        for f in d.rglob("*.*"):
            if f.suffix.lower() not in (".txt", ".gui"):
                continue
            text = read_text(f)
            for gfx in re.findall(r"\b(GFX_[A-Za-z0-9_]+)\b", text):
                used.add(gfx)
                usage_locations[gfx].append(f.relative_to(MOD_ROOT).as_posix())

    missing = sorted(used - defined)
    for gfx in missing:
        locs = ", ".join(sorted(set(usage_locations[gfx]))[:3])
        print(f"  {gfx} usado em [{locs}] mas nao encontrado em nenhum .gfx")
    print(f"Total: {len(missing)} referencia(s) GFX sem definicao encontrada "
          f"(heuristico - nao cobre icones vanilla herdados fora das pastas varridas).")


# ---------------------------------------------------------------------------
# 8. Arquivos vazios relevantes
# ---------------------------------------------------------------------------
def check_empty_files():
    section("Arquivos vazios relevantes (0 bytes)")
    exts = {".txt", ".yml", ".gfx", ".gui", ".lua"}
    skip_dirs = {"_backup_original", ".git"}
    empty = []
    for f in MOD_ROOT.rglob("*"):
        if not f.is_file() or f.suffix.lower() not in exts:
            continue
        if any(part in skip_dirs for part in f.parts):
            continue
        if f.stat().st_size == 0:
            empty.append(f.relative_to(MOD_ROOT).as_posix())
    for rel in sorted(empty):
        print(f"  {rel}")
    print(f"Total: {len(empty)} arquivo(s) vazio(s) (apenas listados - nada foi apagado).")


# ---------------------------------------------------------------------------
# 9. Pastas/arquivos .disabled
# ---------------------------------------------------------------------------
def check_disabled():
    section("Pastas/arquivos .disabled encontrados")
    found = []
    for p in MOD_ROOT.rglob("*.disabled*"):
        found.append(p.relative_to(MOD_ROOT).as_posix())
    for rel in sorted(found):
        print(f"  {rel}")
    print(f"Total: {len(found)} item(ns) .disabled (nao foram tocados).")


# ---------------------------------------------------------------------------
# 10. Building declarado num state que nao possui a provincia
# ---------------------------------------------------------------------------
def check_state_building_mismatch():
    section("Buildings referenciando provincia fora do state")
    sdir = MOD_ROOT / "history" / "states"
    total = 0
    for f in sorted(sdir.glob("*.txt")):
        text = read_text(f)
        m_id = re.search(r"\bid\s*=\s*(\d+)", text)
        state_id = m_id.group(1) if m_id else "?"

        m_prov = re.search(r"provinces\s*=\s*\{([^}]*)\}", text)
        if not m_prov:
            continue
        provinces = set(int(x) for x in re.findall(r"\d+", m_prov.group(1)))

        m_build = re.search(r"buildings\s*=\s*\{(.*?)\n\t\t\}", text, re.S)
        if not m_build:
            continue
        for pid_str in re.findall(r"^\s*(\d+)\s*=\s*\{", m_build.group(1), re.M):
            pid = int(pid_str)
            if pid not in provinces:
                print(f"  {f.name} (state {state_id}): building declarado para provincia {pid}, "
                      f"que nao esta na lista de provinces deste state")
                total += 1
    print(f"Total: {total} inconsistencia(s) de building fora do state.")


def main():
    print(f"Validando mod em: {MOD_ROOT}")
    tag_to_file = check_country_tags()
    check_history_countries(set(tag_to_file.keys()))
    check_localisation_duplicates()
    check_focus_id_duplicates()
    check_event_id_duplicates()
    check_gfx_references()
    check_empty_files()
    check_disabled()
    check_state_building_mismatch()
    print("\nValidacao concluida.")


if __name__ == "__main__":
    sys.exit(main())
