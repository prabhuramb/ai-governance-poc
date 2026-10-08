# AI Governance Control Gate - Proof-of-Concept

A small, self-contained demonstration of three control domains from the
Exhibit 23.4 control matrix: the pre-deployment evaluation gate, model
change control, and evidence retention/traceability.

## What this demonstrates

Three candidate "releases" are evaluated against fixed thresholds
(accuracy, adversarial leak rate, latency). Two of the three releases use
the **real, already-measured leak rates from Exhibit 23.6** (67% baseline,
0% hardened) as actual gate input -- this isn't fabricated data, it's your
prior demonstrated result being used as a real evaluation metric. The
third release is a fabricated regression case: higher accuracy, but a
reintroduced leak, included specifically to test whether the gate correctly
blocks it despite the accuracy improvement.

## Requirements

Python 3.9+, standard library only. No installs, fully deterministic, no
internet connection needed.

## Running it

```
python run_poc.py
```

Takes a couple of seconds. Writes:
- `results.json` -- all three decisions, the change log, and validation checks
- `evidence_log.json` -- the retained evidence record for each release

## What to check

1. Confirm `hardened-v3-regression` was BLOCKED despite having *higher*
   accuracy than `hardened-v2` -- this is the key finding: the gate
   enforces every threshold, not just the one that improved.
2. Confirm `evidence_retrievable_count` is 3/3 and `change_log_completeness`
   shows both non-initial releases have a complete linked record.
3. Fill in `EXHIBIT_24_7_DRAFT.md` with your own explanation, in your own
   words, of what this demonstrates and why it matters.
