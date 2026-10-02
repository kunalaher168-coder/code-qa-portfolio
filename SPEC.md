# Public example specification

Given a list of valid half-open integer intervals `[start, end)` with `start < end`, return their union as sorted, maximal half-open intervals. Intervals that overlap **or touch at an endpoint** must be merged. Duplicate intervals must not appear twice in the result. An empty input returns an empty list.

Examples:

| Input | Required output | Reason |
| --- | --- | --- |
| `[]` | `[]` | No intervals |
| `[(0, 1), (1, 2)]` | `[(0, 2)]` | Endpoint touch |
| `[(3, 5), (1, 4)]` | `[(1, 5)]` | Overlap and unsorted input |
| `[(0, 1), (2, 3)]` | `[(0, 1), (2, 3)]` | Positive gap |

This specification is invented for this portfolio.
