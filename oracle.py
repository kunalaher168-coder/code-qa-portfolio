"""Independent small-domain oracle using covered integer unit segments."""

from __future__ import annotations


def canonical_union(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Build maximal intervals from all covered [n, n+1) segments.

    Intended for small integer test inputs, not large production ranges.
    """
    covered = sorted({unit for start, end in intervals for unit in range(start, end)})
    if not covered:
        return []
    result: list[tuple[int, int]] = []
    run_start = previous = covered[0]
    for unit in covered[1:]:
        if unit != previous + 1:
            result.append((run_start, previous + 1))
            run_start = unit
        previous = unit
    result.append((run_start, previous + 1))
    return result
