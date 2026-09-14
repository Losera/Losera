#!/usr/bin/env python3
"""Render GitHub's public contribution calendar in the profile signal palette."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import urllib.request
from dataclasses import dataclass
from pathlib import Path


PALETTE = ("#15131a", "#4b1628", "#7d1f38", "#bd2449", "#ff3158")
CELL = 10
GAP = 3
LEFT = 34
TOP = 28

DAY_RE = re.compile(
    r'<td[^>]*data-date="(?P<date>\d{4}-\d{2}-\d{2})"[^>]*'
    r'id="(?P<id>[^"]+)"[^>]*data-level="(?P<level>[0-4])"[^>]*>'
)
TOOLTIP_RE = re.compile(
    r'<tool-tip[^>]*for="(?P<id>[^"]+)"[^>]*>(?P<count>\d+) contribution(?:s)?[^<]*</tool-tip>'
)


@dataclass(frozen=True)
class Day:
    date: dt.date
    level: int
    count: int


def fetch_calendar(username: str) -> str:
    url = f"https://github.com/users/{username}/contributions"
    request = urllib.request.Request(url, headers={"User-Agent": "Losera-profile-renderer/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def parse_calendar(source: str) -> list[Day]:
    counts = {match["id"]: int(match["count"]) for match in TOOLTIP_RE.finditer(source)}
    days = [
        Day(
            date=dt.date.fromisoformat(match["date"]),
            level=int(match["level"]),
            count=counts.get(match["id"], 0),
        )
        for match in DAY_RE.finditer(source)
    ]
    if not days:
        raise ValueError("GitHub response contained no contribution days")
    return sorted(days, key=lambda day: day.date)


def render_svg(days: list[Day], username: str) -> str:
    first = days[0].date
    first_sunday = first - dt.timedelta(days=(first.weekday() + 1) % 7)
    week_count = max((day.date - first_sunday).days // 7 for day in days) + 1
    width = LEFT + week_count * (CELL + GAP) + 8
    height = TOP + 7 * (CELL + GAP) + 24
    total = sum(day.count for day in days)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">GitHub contribution signal</title>',
        f'<desc id="desc">{total} public contributions by {html.escape(username)} '
        f'from {days[0].date.isoformat()} through {days[-1].date.isoformat()}</desc>',
        '<rect width="100%" height="100%" rx="8" fill="#07080d"/>',
        '<g font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="9" fill="#8f8999">',
        f'<text x="{LEFT}" y="14" fill="#ff3158" letter-spacing="1.5">CONTRIBUTION SIGNAL / {total:04d}</text>',
    ]

    previous_month = None
    for day in days:
        week = (day.date - first_sunday).days // 7
        if day.date.day <= 7 and day.date.month != previous_month:
            x = LEFT + week * (CELL + GAP)
            parts.append(f'<text x="{x}" y="25">{day.date.strftime("%b").upper()}</text>')
            previous_month = day.date.month

    for label, row in (("M", 1), ("W", 3), ("F", 5)):
        y = TOP + row * (CELL + GAP) + 8
        parts.append(f'<text x="12" y="{y}">{label}</text>')
    parts.append("</g>")

    parts.append('<g stroke="#ff3158" stroke-opacity="0.12">')
    for day in days:
        week = (day.date - first_sunday).days // 7
        row = (day.date.weekday() + 1) % 7
        x = LEFT + week * (CELL + GAP)
        y = TOP + row * (CELL + GAP)
        title = f"{day.count} contribution{'s' if day.count != 1 else ''} on {day.date.isoformat()}"
        parts.append(
            f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" '
            f'fill="{PALETTE[day.level]}"><title>{title}</title></rect>'
        )
    parts.extend(("</g>", "</svg>"))
    return "\n".join(parts) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", default="Losera")
    parser.add_argument("--input", type=Path, help="Read saved GitHub HTML instead of the network")
    parser.add_argument("--output", type=Path, default=Path("assets/contributions.svg"))
    args = parser.parse_args()

    source = args.input.read_text(encoding="utf-8") if args.input else fetch_calendar(args.username)
    svg = render_svg(parse_calendar(source), args.username)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    main()
