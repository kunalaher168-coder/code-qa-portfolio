# Code QA Portfolio

A reproducible public example of turning a written requirement into test cases, checking an implementation against an independent oracle, and reporting a defect with a small counterexample. The example specification and candidate code were created for this portfolio. They are not copied from a client task or a private review.

## Featured review

The [qa-review branch](https://github.com/kunalaher168-coder/code-qa-portfolio/tree/qa-review) examines a function that should merge half-open integer intervals into a canonical result. The candidate has an intentional endpoint boundary error: intervals that touch are left separate.

| Review artifact | What it demonstrates |
| --- | --- |
| [Specification](https://github.com/kunalaher168-coder/code-qa-portfolio/blob/qa-review/SPEC.md) | Clear expected behavior and boundary examples |
| [Candidate](https://github.com/kunalaher168-coder/code-qa-portfolio/blob/qa-review/candidate.py) | A small, deliberately faulty implementation to review |
| [Independent oracle](https://github.com/kunalaher168-coder/code-qa-portfolio/blob/qa-review/oracle.py) | Expected output computed through covered unit segments, without repeating the candidate's merge condition |
| [Audit](https://github.com/kunalaher168-coder/code-qa-portfolio/blob/qa-review/audit.py) and [tests](https://github.com/kunalaher168-coder/code-qa-portfolio/blob/qa-review/tests/test_audit.py) | Deterministic boundary checks and exhaustive small-domain comparison |
| [Finding](https://github.com/kunalaher168-coder/code-qa-portfolio/blob/qa-review/FINDING.md) | Reproduction, expected versus actual result, cause, and regression recommendation |

The audit checks **3,616** invented cases and finds **826** mismatches. The first shortest-length failure is `[(0, 1), (1, 2)]`: the required result is `[(0, 2)]`, while the candidate returns two intervals. Those counts describe this deliberately faulty public sample, not a private codebase.

## Review path

1. Read the [specification](https://github.com/kunalaher168-coder/code-qa-portfolio/blob/qa-review/SPEC.md) and form an expected result for the endpoint case.
2. Inspect the candidate and oracle to see that they use different methods.
3. Run `python audit.py` and `python -m unittest discover -s tests -v` from the `qa-review` branch.
4. Read the [finding](https://github.com/kunalaher168-coder/code-qa-portfolio/blob/qa-review/FINDING.md) as the review deliverable.
