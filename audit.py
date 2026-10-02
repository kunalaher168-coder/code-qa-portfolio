"""Compare the public candidate with an independent oracle on small cases."""

from __future__ import annotations

from itertools import product
import json

from candidate import merge_intervals
from oracle import canonical_union


def cases():
    """Yield shorter cases first so the first failure is easy to reproduce."""
    intervals = [(start, end) for start in range(5) for end in range(start + 1, 6)]
    yield []
    for length in (1, 2, 3):
        for combination in product(intervals, repeat=length):
            yield list(combination)


def run_audit() -> dict[str, object]:
    checked = 0
    mismatches = 0
    first_failure: dict[str, object] | None = None
    for case in cases():
        checked += 1
        expected = canonical_union(case)
        actual = merge_intervals(case)
        if actual != expected:
            mismatches += 1
            if first_failure is None:
                first_failure = {"input": case, "expected": expected, "actual": actual}
    return {
        "dataset": "invented small integer intervals",
        "cases_checked": checked,
        "mismatches": mismatches,
        "first_failure": first_failure,
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2))
