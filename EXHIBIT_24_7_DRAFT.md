# EXHIBIT 24.7 — AI GOVERNANCE CONTROL GATE: DEMONSTRATED PROOF-OF-CONCEPT
[DRAFT — read closely, verify every sentence against your own understanding,
and rewrite anything that isn't genuinely in your own words before this goes
anywhere near the petition.]

Author: Prabhuram Balaraman
Status: Demonstrated proof-of-concept, self-built and self-measured, run on
my own equipment outside of and unconnected to any employer engagement
Extends: Three control domains from the control matrix specified at
Exhibit 24.4 (pre-deployment evaluation gate, model and configuration
change control, and evidence retention and traceability), and the
release-gating discipline demonstrated at Exhibit 24.1, Part B
Supports: Section IV.D of the Brief in Support of Petition (proposed
endeavor, component three)

## 1. Summary

I built a small governance pipeline that evaluates candidate AI-component
releases against fixed thresholds, records evidence of each decision, and
maintains a change log linking each release to what it changed and how it
was re-evaluated. I evaluated three candidate releases, two of which used
the actual, previously-measured leak rates from Exhibit 24.6 (67% baseline,
0% hardened) as real evaluation input rather than fabricated data. The gate
authorized the one release meeting every threshold and blocked the other
two -- including a third, fabricated release with higher measured accuracy
than the authorized one, specifically because it reintroduced a leak. All
evidence was retrievable by version, and the change log was complete for
every non-initial release.

## 2. Purpose and scope

Exhibit 24.4 specified a control matrix in the abstract, covering five
control domains. This proof-of-concept operationalizes three of them: the
pre-deployment evaluation gate (row 1), model and configuration change
control (row 2), and evidence retention and traceability (row 3). It does
not address post-deployment monitoring/drift detection (row 4) or control
mapping/consolidation (row 5), and I do not present it as doing so.

## 3. System under test

The system is a small governance pipeline I built myself: a gate that
evaluates a release's metrics against three fixed thresholds (minimum
accuracy, maximum adversarial leak rate, maximum latency), an evidence log
that records every decision and makes it retrievable by version, and a
change-control module that links each release to its predecessor and the
re-evaluation result that followed.

Two of the three candidate releases evaluated use real data: the
adversarial leak rates for "baseline-v1" and "hardened-v2" are the actual
measured results from Exhibit 24.6 (10 of 15 adversarial-case instances
leaked at baseline; 0 of 15 leaked hardened), not fabricated figures. The
third candidate, "hardened-v3-regression," is fabricated for this
demonstration: it models a release with improved accuracy but a
reintroduced leak, included specifically to test whether the gate would be
swayed by the accuracy improvement alone.

## 4. Method

For each candidate release, the gate evaluates three metrics against fixed
thresholds -- accuracy must be at least 90%, adversarial leak rate must be
0%, and latency must not exceed 500ms -- and authorizes only if every
threshold is met. Each decision is recorded in an evidence log with the
release's full metrics, the decision, and the reasons for any block,
retrievable by version. A change-control record links each release (except
the first, which has no predecessor) to the version it was based on and
the re-evaluation decision that followed.

## 5. Measured outcomes

Results from a run conducted on September 24, 2026:

| Release | Accuracy | Adversarial leak rate | Decision |
|---|---|---|---|
| baseline-v1 | 94% | 66.7% (Exhibit 24.6 baseline, actual) | BLOCKED — leak rate exceeds threshold |
| hardened-v2 | 93% | 0% (Exhibit 24.6 hardened, actual) | AUTHORIZED |
| hardened-v3-regression | 95% | 13% (fabricated regression case) | BLOCKED — leak rate exceeds threshold |

| Validation check | Result |
|---|---|
| Gate decisions deterministic (re-run same input) | True, for all 3 releases |
| Evidence retrievable by version | 3 / 3 |
| Change-log completeness (non-initial releases with linked record) | 2 / 2 |
| Regression correctly blocked despite higher accuracy than the authorized release | True |

The last row is the finding I'd draw the most attention to: hardened-v3-regression
had the highest accuracy of the three candidates (95%, versus 93% for the
authorized release), and the gate still blocked it, because a gate that
only tracked accuracy would have authorized a release with a real security
regression. This is the concrete difference between a threshold on one
metric and a governance gate that enforces all of them together.

## 6. Basis of the figures, and what they do not establish

- The adversarial leak rates for baseline-v1 and hardened-v2 are the
  actual measured results from Exhibit 24.6, not invented for this
  exhibit. The accuracy and latency figures for all three releases, and
  all metrics for hardened-v3-regression, are fabricated for this
  demonstration.
- This demonstration used three candidate releases and three threshold
  criteria. A production governance system would need to handle many more
  releases, more evaluation metrics, and more complex threshold logic
  (e.g., different thresholds for different component types). I do not
  claim this proof-of-concept validates the approach at that scale.
- The gate's determinism check confirms that re-running the same input
  produces the same decision; it does not test the gate's behavior on
  inputs it has not seen, or its robustness to malformed or adversarial
  evaluation reports.
- This exhibit does not address post-deployment monitoring, drift
  detection, or the control-mapping/consolidation domains from Exhibit
  24.4's control matrix, and I do not present it as covering them.
- This is a small, self-contained demonstration, not a production
  governance system, and I do not present it as comprehensive coverage of
  AI governance requirements.

## 7. Relevance to the proposed endeavor

This exhibit demonstrates that three of the five control domains specified
at Exhibit 24.4 can be operationalized into a working, deterministic
pipeline, using the same evidentiary discipline as the rest of Exhibit 24:
a stated method, a stated result, and a stated basis. It also demonstrates
something specific to governance work: that a gate enforcing multiple
thresholds together catches a regression that a gate tracking only one
metric would miss. By using the actual measured leak rates from Exhibit
24.6 as real input rather than fabricated data, this exhibit also shows
the endeavor's components functioning together -- the security validation
result from one component feeding a real decision in another -- rather
than as three unconnected demonstrations.
