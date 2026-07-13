#!/usr/bin/env python3
"""Read-only analysis: find where non-existent country tags are still referenced.

Run from anywhere: `python tools/find_missing_tag_sources.py`. Only prints a
report, classified by file / field context / distinct-tag count. Never
modifies any file, never guesses which Azarya tag a vanilla tag "should"
become.

Exit code is always 0 (this is a report tool, not a validator).
"""
import re
import sys
from pathlib import Path

MOD_ROOT = Path(__file__).resolve().parent.parent
COUNTRY_TAGS_DIR = MOD_ROOT / "common" / "country_tags"

SKIP_DIR_SUBSTR = (".disabled", "doctrines.disabled", ".git")
SKIP_FILE_SUBSTR = ("_documentation", "report", ".md", "desktop.ini")

# Tokens that match the [A-Z]{2,4} shape but are not country tags.
NOISE_TOKENS = {
    "GFX", "NOT", "AND", "OR", "ROOT", "FROM", "PREV", "THIS", "YES", "NO",
    "SP", "TODO", "RULE", "FREE", "SAME", "TEXT", "AI", "ICON", "SPAN",
    "ELSE", "ONE", "CAS", "XSM", "EU", "ID", "IF",
}

# field/context -> compiled pattern. Group 1 (or the {...} body) holds tag(s).
SINGLE_TAG_CONTEXTS = {
    "original_tag":  re.compile(r"\boriginal_tag\s*=\s*([A-Z]{2,4})\b"),
    "tag":           re.compile(r"(?<![A-Za-z_])\btag\s*=\s*([A-Z]{2,4})\b"),
    "is_ally_with":  re.compile(r"\bis_ally_with\s*=\s*([A-Z]{2,4})\b"),
    "has_war_with":  re.compile(r"\bhas_war_with\s*=\s*([A-Z]{2,4})\b"),
    "is_subject_of": re.compile(r"\bis_subject_of\s*=\s*([A-Z]{2,4})\b"),
    "controller":    re.compile(r"\bcontroller\s*=\s*([A-Z]{2,4})\b"),
    "owner":         re.compile(r"\bowner\s*=\s*([A-Z]{2,4})\b"),
}

LIST_CONTEXTS = {
    "blocked_for/available_for": re.compile(r"(?:blocked_for|available_for)\s*=\s*\{([^{}]*)\}"),
    "technology_sharing_countries": re.compile(r"\bcountries\s*=\s*\{([^{}]*)\}"),
}

COMMENT_RE = re.compile(r"#.*")


def load_valid_tags() -> set[str]:
    tags: set[str] = set()
    static_file = COUNTRY_TAGS_DIR / "00_countries.txt"
    if static_file.exists():
        for line in static_file.read_text(encoding="utf-8-sig", errors="ignore").splitlines():
            m = re.match(r"\s*([A-Z0-9]{2,4})\s*=", line)
            if m:
                tags.add(m.group(1))
    dyn_file = COUNTRY_TAGS_DIR / "zz_dynamic_countries.txt"
    if dyn_file.exists():
        for line in dyn_file.read_text(encoding="utf-8-sig", errors="ignore").splitlines():
            m = re.match(r"\s*(D\d{2})\s*=", line)
            if m:
                tags.add(m.group(1))
    return tags


def strip_comments(content: str) -> str:
    return "\n".join(COMMENT_RE.sub("", line) for line in content.splitlines())


def iter_loadable_txt_files():
    for path in MOD_ROOT.rglob("*.txt"):
        rel = path.relative_to(MOD_ROOT)
        parts = rel.parts
        if any(any(s in part for s in SKIP_DIR_SUBSTR) for part in parts[:-1]):
            continue
        if any(s in path.name for s in SKIP_FILE_SUBSTR):
            continue
        if ".disabled" in path.name:
            continue
        yield path


def main() -> int:
    valid_tags = load_valid_tags()
    if not valid_tags:
        print("ERRO: nao foi possivel carregar tags validas de common/country_tags/. Abortando.")
        return 1
    print(f"Tags validas carregadas: {len(valid_tags)} (57 estaticas + D01-D50 dinamicas esperadas)\n")

    # tag -> file -> set(context)
    hits: dict[str, dict[str, set[str]]] = {}
    files_scanned = 0

    for path in iter_loadable_txt_files():
        files_scanned += 1
        try:
            raw = path.read_text(encoding="utf-8-sig", errors="ignore")
        except Exception:
            continue
        content = strip_comments(raw)
        rel = str(path.relative_to(MOD_ROOT))

        for ctx_name, pat in SINGLE_TAG_CONTEXTS.items():
            for m in pat.finditer(content):
                tag = m.group(1)
                if tag in valid_tags or tag in NOISE_TOKENS:
                    continue
                hits.setdefault(tag, {}).setdefault(rel, set()).add(ctx_name)

        for ctx_name, pat in LIST_CONTEXTS.items():
            for m in pat.finditer(content):
                for tag in re.findall(r"\b([A-Z]{2,4})\b", m.group(1)):
                    if tag in valid_tags or tag in NOISE_TOKENS:
                        continue
                    hits.setdefault(tag, {}).setdefault(rel, set()).add(ctx_name)

    print(f"Arquivos .txt carregaveis analisados: {files_scanned}\n")

    # file -> set(tags)
    file_tags: dict[str, set[str]] = {}
    for tag, files in hits.items():
        for f in files:
            file_tags.setdefault(f, set()).add(tag)

    print("=== Arquivos com mais tags distintas inexistentes (carga concentrada) ===")
    for f, tags in sorted(file_tags.items(), key=lambda x: -len(x[1]))[:40]:
        print(f"  {len(tags):3d}  {f}")

    print()
    print("=== Contextos por tipo (total de ocorrencias) ===")
    ctx_totals: dict[str, int] = {}
    for tag, files in hits.items():
        for f, ctxs in files.items():
            for c in ctxs:
                ctx_totals[c] = ctx_totals.get(c, 0) + 1
    for c, n in sorted(ctx_totals.items(), key=lambda x: -x[1]):
        print(f"  {n:4d}  {c}")

    print()
    print(f"Total de tags distintas inexistentes encontradas: {len(hits)}")
    print(f"Total de arquivos envolvidos: {len(file_tags)}")

    print()
    print("=== Detalhe por tag (arquivo: contextos) ===")
    for tag in sorted(hits):
        print(f"\n{tag}:")
        for f, ctxs in sorted(hits[tag].items()):
            print(f"  {f}  [{', '.join(sorted(ctxs))}]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
