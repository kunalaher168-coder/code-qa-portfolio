# Review finding - endpoint equality is omitted

**Public example only.** The candidate and task were created for this portfolio.

## Reproduction

Input: `[(0, 1), (1, 2)]`

Expected: `[(0, 2)]`

Actual: `[(0, 1), (1, 2)]`

The specification requires touching intervals to form one maximal interval. The candidate tests `start < previous_end`, which handles overlap but excludes equality. The condition should include equality. The independent oracle builds covered unit segments and joins consecutive segments, so it does not rely on the candidate's merge condition.

## Review method

1. Convert the written requirements into explicit boundary cases: empty input, overlap, endpoint touch, gap, duplicates, and input order.
2. Compare the candidate with a separately implemented oracle on all interval lists of length up to three in a small domain.
3. Report the shortest failing input with expected and actual outputs.
4. Add a regression case for the endpoint equality rule before changing the implementation.

`audit.py` is deterministic and reports how many small cases disagree. A passing small-domain audit would still need broader tests and code review before production use.
