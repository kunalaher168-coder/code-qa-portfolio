from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from audit import run_audit
from candidate import merge_intervals
from oracle import canonical_union


class CodeReviewTests(unittest.TestCase):
    def test_independent_oracle_examples(self) -> None:
        self.assertEqual(canonical_union([]), [])
        self.assertEqual(canonical_union([(0, 1), (1, 2)]), [(0, 2)])
        self.assertEqual(canonical_union([(3, 5), (1, 4)]), [(1, 5)])
        self.assertEqual(canonical_union([(0, 1), (2, 3)]), [(0, 1), (2, 3)])

    def test_minimal_reproducible_failure(self) -> None:
        case = [(0, 1), (1, 2)]
        self.assertEqual(merge_intervals(case), [(0, 1), (1, 2)])
        self.assertNotEqual(merge_intervals(case), canonical_union(case))

    def test_audit_finds_boundary_defect(self) -> None:
        report = run_audit()
        self.assertEqual(report["dataset"], "invented small integer intervals")
        self.assertEqual(report["cases_checked"], 3616)
        self.assertGreater(report["mismatches"], 0)
        self.assertEqual(report["first_failure"]["input"], [(0, 1), (1, 2)])
        self.assertEqual(report["first_failure"]["expected"], [(0, 2)])


if __name__ == "__main__":
    unittest.main()
