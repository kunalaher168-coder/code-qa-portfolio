# Code QA review - public work sample

This branch demonstrates a small review from specification to reproducible defect. The task, candidate implementation, and tests were written independently for public display. They contain no private coding prompt, rubric, client code, or trace.

The invented task is to merge half-open integer intervals into a canonical result. The candidate has one intentional boundary error. `audit.py` checks curated and exhaustive small cases against an independent unit-segment oracle and prints a minimal counterexample.

## Run

```powershell
python audit.py
python -m unittest discover -s tests -v
```

Read [SPEC.md](SPEC.md) for the expected behavior and [FINDING.md](FINDING.md) for the review note. The candidate is deliberately faulty so the QA process has a defect to find; it is not a submission or a sample of private code.
