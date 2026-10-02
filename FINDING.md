# Review Finding: Endpoint Equality Is Omitted

**Public example only.** The candidate and task were created for this portfolio.

## Reproduction

Input: `[(0, 1), (1, 2)]`

Expected: `[(0, 2)]`

Actual: `[(0, 1), (1, 2)]`

The specification requires touching intervals to form one maximal interval. The candidate tests `start < previous_end`, which handles overlap but excludes equality. The returned intervals represent the same set of points, but violate the specified canonical format. A consumer comparing normalized interval lists could therefore receive an incorrect result.

## Cause and recommended correction

The merge condition should include equality: `start <= previous_end`. Add the endpoint-touch case above as a regression test. The independent oracle builds covered unit segments and joins consecutive segments, so it does not repeat the candidate's merge condition.

## Review method

1. Convert the written requirements into explicit boundary cases: empty input, overlap, endpoint touch, gap, duplicates, and input order.
2. Compare the candidate with a separately implemented oracle on all interval lists of length up to three in a small domain.
3. Report the first shortest-length failing input in the bounded search, with expected and actual outputs.
4. Add a regression case for the endpoint equality rule before changing the implementation.

`audit.py` is deterministic: 826 of 3,616 generated cases disagree with the intentionally faulty candidate. This is a demonstration finding, not a report about a private or production system. A passing small-domain audit after a fix would still need broader tests and review before production use.
