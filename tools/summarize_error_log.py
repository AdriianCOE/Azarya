#!/usr/bin/env python3
"""Summarize a HOI4 error.log without modifying it.

Usage:
    python tools/summarize_error_log.py <path-to-error.log> [--markdown tools/reports/error_log_summary.md]

Groups log entries two ways:
  - "detailed" signature: keeps the specific token/tech/idea/tag/sprite/etc. name.
  - "broad family": functional category (invalid_technology_reference, invalid_idea_reference, ...).

Only normalizes: timestamps, line numbers explicitly tied to "line"/"near line"/"line :",
memory addresses, and absolute machine paths (collapsed to the relative mod path).
Everything else (file paths, token/trigger/effect/tech/idea/tag/sprite/specialization/
state/province/resource names) is preserved as-is.

Read-only. Never modifies the input log or any mod file.
"""
import argparse
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

LINE_RE = re.compile(r'^\[(?P<time>[\d:]+)\]\[(?P<date>[^\]]+)\]\[(?P<src>[^\]]+)\]:\s*(?P<msg>.*)$')

# absolute machine path prefix -> collapse to relative
ABS_PATH_RE = re.compile(r'[A-Za-z]:[\\/](?:[^"\s]+[\\/])*mod[\\/][^\\/"\s]+[\\/]', re.IGNORECASE)


def read_entries(path: Path):
    """Read the log and merge continuation lines (lines without the
    [time][date][src]: prefix) into the previous logical entry."""
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        raw_lines = f.readlines()

    entries = []
    for line in raw_lines:
        line = line.rstrip("\n")
        m = LINE_RE.match(line)
        if m:
            entries.append({
                "time": m.group("time"),
                "date": m.group("date"),
                "src": m.group("src"),
                "msg": m.group("msg"),
            })
        elif entries and line.strip():
            entries[-1]["msg"] += " | " + line.strip()
    return raw_lines, entries


def normalize(msg: str) -> str:
    m = msg
    m = ABS_PATH_RE.sub("", m)
    m = re.sub(r'near line:\s*\d+', 'near line: N', m)
    m = re.sub(r'\bline\s*:\s*\d+', 'line: N', m)
    m = re.sub(r'\bline\s+\d+', 'line N', m)
    m = re.sub(r':\d+:', ':N:', m)  # "file.txt:217:" -> "file.txt:N:"
    m = re.sub(r'0x[0-9A-Fa-f]+', '0xN', m)
    return m.strip()


def extract_origin_file(msg: str, src: str) -> str:
    fm = re.search(r'([\w./\\-]+\.(?:txt|gui|gfx|lua|yml|dds|asset))', msg)
    return fm.group(1) if fm else src


FAMILY_RULES = [
    ("missing_country_tag", re.compile(r"is not in the tag list")),
    ("invalid_specialization", re.compile(r"specialization", re.I)),
    ("missing_special_project_reward", re.compile(r"\bsp_[a-z_]+|Special Project", re.I)),
    ("invalid_scientist_trait", re.compile(r"scientist trait|scientist_traits", re.I)),
    ("invalid_technology_reference", re.compile(r"has_tech|Invalid tech|common/technologies", re.I)),
    ("invalid_trigger_doctrine", re.compile(r"doctrines|regimental_support|_battery\b|fire_support|field_guns", re.I)),
    ("invalid_faction_goal", re.compile(r"faction_goal|faction_manifest|faction_template|Faction goal|is_chinese_country", re.I)),
    ("invalid_raid_reference", re.compile(r"common/raids|bathe_in_hellfire|cobalt_sea|great_wall|is_literally_china", re.I)),
    ("invalid_technology_sharing", re.compile(r"technology_sharing", re.I)),
    ("invalid_decision_reference", re.compile(r"common/decisions", re.I)),
    ("invalid_idea_reference", re.compile(r"has_idea|is not [Aa] valid Idea", re.I)),
    ("missing_gfx_sprite", re.compile(r"GUI_TYPE|sprite type|\.gui\b|\.gfx\b|containerwindow|gui\.cpp", re.I)),
    ("missing_texture_asset", re.compile(r"texture|\.dds\b|Unexpected token: DDS", re.I)),
    ("duplicate_audio", re.compile(r"[Ss]ound|audio", re.I)),
    ("duplicate_entity", re.compile(r"Duplicate of|pdx_entity", re.I)),
    ("map_state_issue", re.compile(r"gamestate\.cpp|state.*building|Net has too many|statehistory", re.I)),
    ("localisation_issue", re.compile(r"localisation|loc key|missing localisation", re.I)),
]


def classify_family(src: str, msg: str) -> str:
    combined = src + " " + msg
    for name, pat in FAMILY_RULES:
        if pat.search(combined):
            return name
    return "outros"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("log_path", type=Path)
    ap.add_argument("--markdown", type=Path, default=None,
                     help="optional path to write a Markdown report (e.g. tools/reports/error_log_summary.md)")
    ap.add_argument("--top", type=int, default=50, help="how many detailed signatures to show (default 50)")
    args = ap.parse_args()

    raw_lines, entries = read_entries(args.log_path)

    detailed_sigs = Counter()
    detailed_example = {}
    family_counter = Counter()
    family_detail = defaultdict(Counter)
    origin_files = Counter()

    for e in entries:
        norm_msg = normalize(e["msg"])
        origin = extract_origin_file(e["msg"], e["src"])
        origin_files[origin] += 1

        key = (e["src"], norm_msg)
        detailed_sigs[key] += 1
        detailed_example.setdefault(key, e["msg"][:200])

        family = classify_family(e["src"], e["msg"])
        family_counter[family] += 1
        family_detail[family][(e["src"], norm_msg)] += 1

    total_raw = len(raw_lines)
    total_entries = len(entries)
    total_sigs = len(detailed_sigs)

    lines_out = []

    def emit(s=""):
        print(s)
        lines_out.append(s)

    emit(f"Log: {args.log_path}")
    emit(f"Linhas brutas: {total_raw}")
    emit(f"Entradas logicas (apos mesclar continuacao multilinha): {total_entries}")
    emit(f"Assinaturas detalhadas unicas: {total_sigs}")
    if entries:
        emit(f"Primeiro timestamp: {entries[0]['date']} {entries[0]['time']}")
        emit(f"Ultimo timestamp: {entries[-1]['date']} {entries[-1]['time']}")

    emit(f"\n=== Top {args.top} assinaturas detalhadas ===")
    for (src, norm), count in detailed_sigs.most_common(args.top):
        emit(f"{count}\t[{src}]\t{norm[:180]}")

    emit(f"\n=== Top 20 arquivos de origem ===")
    for f, count in origin_files.most_common(20):
        emit(f"{count}\t{f}")

    emit(f"\n=== Familias amplas ===")
    total_classified = sum(family_counter.values())
    for family, count in family_counter.most_common():
        pct = 100 * count / total_classified if total_classified else 0
        emit(f"{count}\t{pct:.1f}%\t{family}")

    emit(f"\n=== Detalhe por familia (top 5 assinaturas dentro de cada uma) ===")
    for family, _ in family_counter.most_common():
        emit(f"\n-- {family} --")
        for (src, norm), count in family_detail[family].most_common(5):
            emit(f"  {count}\t[{src}]\t{norm[:150]}")

    top5 = sum(c for _, c in detailed_sigs.most_common(5))
    emit(f"\nTop 5 assinaturas = {100*top5/total_entries:.1f}% do total ({top5}/{total_entries})" if total_entries else "")

    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        with open(args.markdown, "w", encoding="utf-8") as f:
            f.write("# Resumo do error.log\n\n```\n")
            f.write("\n".join(lines_out))
            f.write("\n```\n")
        print(f"\nRelatorio Markdown salvo em: {args.markdown}")


if __name__ == "__main__":
    sys.exit(main())
