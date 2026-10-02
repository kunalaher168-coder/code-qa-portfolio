# Code QA Review Exercise

This public exercise follows a small review from requirement to finding. The task, candidate, and tests were created for this portfolio. The candidate contains a deliberate boundary defect so the review process has a concrete issue to identify. Nothing here is copied from a private prompt, rubric, codebase, or trace.

## Requirement under review

Given valid half-open integer intervals, return sorted, maximal intervals representing their union. Intervals that overlap or touch at an endpoint must be merged. The full public contract and examples are in [SPEC.md](SPEC.md).

## Review process

| Step | Artifact | Purpose |
| --- | --- | --- |
| State the contract | [SPEC.md](SPEC.md) | Make endpoint behavior, ordering, duplicates, and empty input explicit |
| Inspect the implementation | [candidate.py](candidate.py) | Identify branches and comparisons that could violate the contract |
| Build an independent expectation | [oracle.py](oracle.py) | Expand small integer ranges into covered unit segments, then reconstruct maximal intervals |
| Exercise edge cases | [tests/test_audit.py](tests/test_audit.py) | Check touching, overlap, gaps, order, and the audit result |
| Search a bounded space | [audit.py](audit.py) | Compare candidate and oracle across every list of up to three intervals drawn from endpoints 0 through 5 |
| Communicate the defect | [FINDING.md](FINDING.md) | Give a minimal reproduction, expected and actual results, cause, and regression recommendation |

## Result

The deterministic audit checks **3,616** invented cases and finds **826** candidate-oracle mismatches. Its first shortest-length failure is `[(0, 1), (1, 2)]`. The required result is `[(0, 2)]`; the candidate returns the two intervals separately. The returned union covers the same points, but it is not the canonical output required by the specification.

## Reproduce

Use Python 3.11 and the standard library:

```powershell
python audit.py
python -m unittest discover -s tests -v
```

The test suite passes when it correctly detects the **intentional** candidate defect. [GitHub Actions](.github/workflows/tests.yml) runs the three tests on pushes to this branch. A passing QA test run does not mean the candidate itself meets the specification.

## Scope

The exhaustive check covers a deliberately small integer domain. It is useful for finding a concise counterexample, but it is not a proof for unbounded production inputs. The [portfolio index](https://github.com/kunalaher168-coder/code-qa-portfolio) explains how to review this sample and links the separate ML and competitive-coding repositories.
