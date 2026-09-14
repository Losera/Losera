import datetime as dt
import unittest
from pathlib import Path

from scripts.render_contributions import PALETTE, parse_calendar, render_svg


FIXTURE = Path(__file__).parent / "fixtures" / "contributions.html"


class ContributionRendererTest(unittest.TestCase):
    def setUp(self) -> None:
        self.days = parse_calendar(FIXTURE.read_text(encoding="utf-8"))

    def test_parses_dates_levels_and_counts(self) -> None:
        self.assertEqual(len(self.days), 3)
        self.assertEqual(self.days[1].date, dt.date(2026, 9, 7))
        self.assertEqual(self.days[1].level, 1)
        self.assertEqual(self.days[1].count, 1)
        self.assertEqual(self.days[2].count, 12)

    def test_renders_accessible_palette_svg(self) -> None:
        svg = render_svg(self.days, "Losera")
        self.assertIn('role="img"', svg)
        self.assertIn("CONTRIBUTION SIGNAL / 0013", svg)
        self.assertIn("12 contributions on 2026-09-08", svg)
        for color in (PALETTE[0], PALETTE[1], PALETTE[4]):
            self.assertIn(f'fill="{color}"', svg)


if __name__ == "__main__":
    unittest.main()
