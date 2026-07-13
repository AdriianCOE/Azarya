#!/usr/bin/env python3
"""Read-only sanity checks for the Azarya mod tree.

Run from anywhere: `python tools/validate_mod.py`. Only prints findings,
classified as ERROR / WARNING / INFO. Never modifies any file.

Exit code: 1 if any ERROR was found, 0 otherwise.
"""
import re
import sys
from pathlib import Path

MOD_ROOT = Path(__file__).resolve().parent.parent
EXTERNAL_MANIFEST = MOD_ROOT.parent / f"{MOD_ROOT.name}.mod"
DESCRIPTOR = MOD_ROOT / "descriptor.mod"

counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def section(title: str):
    print(f"\n=== {title} ===")


def report(level: str, msg: str):
    counts[level] += 1
    print(f"  [{level}] {msg}")


def parse_replace_paths(text: str) -> list:
    return re.findall(r'replace_path\s*=\s*"([^"]+)"', text)


def parse_field(text: str, field: str):
    # anchored to start-of-line so e.g. "path" doesn't match inside "replace_path"
    m = re.search(rf'^{field}\s*=\s*"([^"]*)"', text, re.M)
    return m.group(1) if m else None


def extract_block(text: str, key: str):
    """Return the raw content between the braces of the first `key = { ... }`
    block, using brace-depth tracking (not naive regex) so nested nested
    numeric keys used as plain values are not mistaken for sibling blocks."""
    m = re.search(rf"\b{re.escape(key)}\s*=\s*{{", text)
    if not m:
        return None
    start = m.end()  # position right after the opening '{'
    depth = 1
    i = start
    while i < len(text) and depth > 0:
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
        i += 1
    if depth != 0:
        return None  # unbalanced, caller's brace-count check will flag it
    return text[start:i - 1]


def direct_numeric_children(block_text: str):
    """Within a block's raw content, find numeric keys that are direct
    children (depth 0 relative to this block), e.g. `1159 = { ... }`."""
    children = []
    depth = 0
    i = 0
    n = len(block_text)
    while i < n:
        c = block_text[i]
        if c == "{":
            depth += 1
            i += 1
            continue
        if c == "}":
            depth -= 1
            i += 1
            continue
        if depth == 0:
            m = re.match(r"\s*(\d+)\s*=\s*\{", block_text[i:])
            if m:
                children.append(int(m.group(1)))
                i += m.end()
                continue
        i += 1
    return children


# ---------------------------------------------------------------------------
# 1/2/10. Manifestos (.mod externo x descriptor.mod) e replace_path
# ---------------------------------------------------------------------------
def check_manifests():
    section("Manifesto externo (.mod) e divergencia com descriptor.mod")

    if not EXTERNAL_MANIFEST.is_file():
        report("WARNING", f"manifesto externo esperado nao encontrado: {EXTERNAL_MANIFEST}")
        ext_text = ""
    else:
        ext_text = read_text(EXTERNAL_MANIFEST)
        ext_path = parse_field(ext_text, "path")
        if ext_path:
            if not Path(ext_path).is_dir():
                report("ERROR", f"'{EXTERNAL_MANIFEST.name}': path=\"{ext_path}\" nao existe")
            elif Path(ext_path).resolve() != MOD_ROOT.resolve():
                report("WARNING", f"'{EXTERNAL_MANIFEST.name}': path=\"{ext_path}\" nao aponta para a raiz atual do mod ({MOD_ROOT})")
        else:
            report("WARNING", f"'{EXTERNAL_MANIFEST.name}' nao tem campo path=")

    if not DESCRIPTOR.is_file():
        report("WARNING", f"descriptor.mod nao encontrado em {DESCRIPTOR}")
        desc_text = ""
    else:
        desc_text = read_text(DESCRIPTOR)

    if ext_text and desc_text:
        ext_name = parse_field(ext_text, "name")
        desc_name = parse_field(desc_text, "name")
        if ext_name != desc_name:
            report("WARNING", f"name diverge: externo=\"{ext_name}\" vs descriptor.mod=\"{desc_name}\"")

        ext_paths = set(parse_replace_paths(ext_text))
        desc_paths = set(parse_replace_paths(desc_text))
        only_ext = sorted(ext_paths - desc_paths)
        only_desc = sorted(desc_paths - ext_paths)
        if only_ext:
            report("WARNING", f"replace_path só no manifesto externo (ausente do descriptor.mod): {', '.join(only_ext)}")
        if only_desc:
            report("WARNING", f"replace_path só no descriptor.mod (ausente do manifesto externo): {', '.join(only_desc)}")
        if not only_ext and not only_desc and ext_name == desc_name:
            print("  Nenhuma divergencia entre os dois manifestos.")

    section("replace_path apontando para subpasta inexistente (nem como .disabled)")
    all_paths = set(parse_replace_paths(desc_text)) if desc_text else set()
    dangling = 0
    for rp in sorted(all_paths):
        active = MOD_ROOT / rp
        disabled_variant = MOD_ROOT / f"{rp}.disabled"
        if not active.exists() and not disabled_variant.exists():
            report("WARNING", f"replace_path=\"{rp}\" nao existe (nem ativo, nem .disabled) - "
                               f"pode ser bloqueio intencional de conteudo vanilla, ou lixo; verificar manualmente")
            dangling += 1
    if dangling == 0:
        print("  Nenhum replace_path totalmente orfao encontrado.")


# ---------------------------------------------------------------------------
# 3. .gui/.gfx carregaveis dentro de pastas de backup
# ---------------------------------------------------------------------------
def check_backup_leftovers():
    section("Arquivos .gui/.gfx carregaveis dentro de pastas de backup")
    found = 0
    for f in MOD_ROOT.rglob("*"):
        if not f.is_file() or f.suffix.lower() not in (".gui", ".gfx"):
            continue
        if any(part.lower().startswith("_backup") for part in f.parts):
            report("ERROR", f"{f.relative_to(MOD_ROOT).as_posix()} tem extensao carregavel dentro de uma pasta de backup")
            found += 1
    if found == 0:
        print("  Nenhum arquivo de backup carregavel encontrado.")


# ---------------------------------------------------------------------------
# 4. DDS sem magic bytes validos
# ---------------------------------------------------------------------------
def check_dds_headers():
    section("Arquivos .dds sem magic bytes 'DDS ' validos")
    bad = 0
    total = 0
    for f in MOD_ROOT.rglob("*.dds"):
        total += 1
        try:
            with open(f, "rb") as fh:
                header = fh.read(4)
        except OSError as e:
            report("ERROR", f"{f.relative_to(MOD_ROOT).as_posix()}: erro ao ler ({e})")
            bad += 1
            continue
        if header != b"DDS ":
            report("ERROR", f"{f.relative_to(MOD_ROOT).as_posix()}: header={header!r} (esperado b'DDS ')")
            bad += 1
    print(f"  {total} arquivo(s) .dds verificados, {bad} invalido(s).")


# ---------------------------------------------------------------------------
# 5/6. Buildings fora do state / provincia em mais de um state
# ---------------------------------------------------------------------------
def check_state_provinces_and_buildings():
    section("Construcao provincial fora do state / provincia em mais de um state")
    sdir = MOD_ROOT / "history" / "states"
    province_owner = {}  # province id -> state file name
    dup_provinces = 0
    bad_buildings = 0

    for f in sorted(sdir.glob("*.txt")):
        text = read_text(f)
        m_id = re.search(r"\bid\s*=\s*(\d+)", text)
        state_id = m_id.group(1) if m_id else "?"

        provinces_block = extract_block(text, "provinces")
        provinces = set(int(x) for x in re.findall(r"\d+", provinces_block)) if provinces_block else set()

        for pid in provinces:
            if pid in province_owner and province_owner[pid] != f.name:
                report("ERROR", f"provincia {pid} declarada em {province_owner[pid]} e tambem em {f.name}")
                dup_provinces += 1
            else:
                province_owner[pid] = f.name

        history_block = extract_block(text, "history") or text
        buildings_block = extract_block(history_block, "buildings")
        if not buildings_block:
            continue
        for pid in direct_numeric_children(buildings_block):
            if pid not in provinces:
                report("ERROR", f"{f.name} (state {state_id}): building declarado para provincia {pid}, "
                                 f"que nao esta na lista de provinces deste state")
                bad_buildings += 1

    print(f"  {bad_buildings} building(s) fora do state, {dup_provinces} provincia(s) duplicada(s) entre states.")


# ---------------------------------------------------------------------------
# 7. Chaves desbalanceadas (contagem simples)
# ---------------------------------------------------------------------------
def check_brace_balance():
    section("Chaves desbalanceadas (contagem simples open/close)")
    dirs = [
        MOD_ROOT / "history" / "units",
        MOD_ROOT / "history" / "countries",
        MOD_ROOT / "history" / "states",
        MOD_ROOT / "common" / "national_focus",
        MOD_ROOT / "events",
    ]
    bad = 0
    for d in dirs:
        if not d.exists():
            continue
        for f in sorted(d.glob("*.txt")):
            text = read_text(f)
            o, c = text.count("{"), text.count("}")
            if o != c:
                report("WARNING", f"{f.relative_to(MOD_ROOT).as_posix()}: {{={o} }}={c} (diferenca={o - c})")
                bad += 1
    if bad == 0:
        print("  Nenhum desbalanceamento de contagem encontrado "
              "(nota: contagem igual NAO garante aninhamento correto).")


# ---------------------------------------------------------------------------
# 8. Tags <-> country files <-> history/countries
# ---------------------------------------------------------------------------
def check_country_tags():
    section("Tags sem country file / country files sem tag / history sem tag valida")
    tags_dir = MOD_ROOT / "common" / "country_tags"
    countries_dir = MOD_ROOT / "common" / "countries"
    hdir = MOD_ROOT / "history" / "countries"

    tag_to_file = {}
    for f in sorted(tags_dir.glob("*.txt")):
        text = read_text(f)
        for m in re.finditer(r'^\s*([A-Z0-9]{3})\s*=\s*"([^"]+)"', text, re.M):
            tag_to_file[m.group(1)] = m.group(2)

    for tag, rel_path in sorted(tag_to_file.items()):
        target = MOD_ROOT / "common" / rel_path
        if not target.is_file():
            report("WARNING", f"tag {tag} -> common/{rel_path} (nao existe)")

    referenced = {Path(p).name for p in tag_to_file.values()}
    for f in sorted(countries_dir.glob("*.txt")):
        if f.name not in referenced:
            report("WARNING", f"common/countries/{f.name} (nenhuma tag aponta para ele)")

    for f in sorted(hdir.glob("*.txt")):
        m = re.match(r"^([A-Z0-9]{2,3})", f.stem)
        tag = m.group(1) if m else None
        if not tag or tag not in tag_to_file:
            report("WARNING", f"history/countries/{f.name} (prefixo de tag '{tag}' nao reconhecido)")

    print(f"  {len(tag_to_file)} tags conhecidas verificadas.")


# ---------------------------------------------------------------------------
# 9. Focus IDs / Event IDs duplicados
# ---------------------------------------------------------------------------
def check_id_duplicates():
    section("Focus IDs duplicados")
    fdir = MOD_ROOT / "common" / "national_focus"
    seen = {}
    for f in sorted(fdir.glob("*.txt")):
        text = read_text(f)
        for m in re.finditer(r"^\s*id\s*=\s*([A-Za-z0-9_.\-]+)", text, re.M):
            fid = m.group(1)
            if fid in seen and seen[fid] != f.name:
                report("ERROR", f"focus id '{fid}' aparece em {seen[fid]} e em {f.name}")
            else:
                seen[fid] = f.name
    print(f"  {len(seen)} focus id(s) unicos vistos.")

    section("Event IDs duplicados")
    edir = MOD_ROOT / "events"
    seen = {}
    for f in sorted(edir.glob("*.txt")):
        text = read_text(f)
        for m in re.finditer(r"^\s*id\s*=\s*([A-Za-z0-9_]+\.\d+)", text, re.M):
            eid = m.group(1)
            if eid in seen and seen[eid] != f.name:
                report("ERROR", f"event id '{eid}' aparece em {seen[eid]} e em {f.name}")
            else:
                seen[eid] = f.name
    print(f"  {len(seen)} event id(s) unicos vistos.")


def main():
    print(f"Validando mod em: {MOD_ROOT}")
    print(f"Manifesto externo esperado em: {EXTERNAL_MANIFEST}")

    check_manifests()
    check_backup_leftovers()
    check_dds_headers()
    check_state_provinces_and_buildings()
    check_brace_balance()
    check_country_tags()
    check_id_duplicates()

    print(f"\nResumo: {counts['ERROR']} ERROR, {counts['WARNING']} WARNING, {counts['INFO']} INFO.")
    return 1 if counts["ERROR"] > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
