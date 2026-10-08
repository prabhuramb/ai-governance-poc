# Insert Package — Integrating Exhibit 23.6 into the Petition

Same pattern as the two prior insert packages. Four edits.

---

## 1. Brief in Support of Petition — append to the end of ¶47

Your current ¶47 ends with: "...to the evaluation gates an AI component
requires."

**Add immediately after that sentence, still within ¶47:**

> The Petitioner has since built and run a small governance pipeline
> operationalizing three of the five control domains specified in the
> matrix above — the pre-deployment evaluation gate, model and
> configuration change control, and evidence retention and traceability —
> submitted at Exhibit 23.6. That pipeline evaluated candidate releases
> using, in part, the actual adversarial leak rates measured at Exhibit
> 23.5 (67% at baseline, 0% hardened) as real evaluation input, and
> correctly blocked a fabricated regression case with higher measured
> accuracy than the authorized release, because that case reintroduced a
> security leak. The Petitioner presents this as a demonstrated
> proof-of-concept for three of the matrix's five control domains, not as
> a claim that post-deployment monitoring or control-mapping/consolidation
> (the remaining two domains) are likewise demonstrated.

---

## 2. Part II — Index of Exhibits — update the Exhibit 24 row

If you've applied both prior edits, your row currently ends: "...23.5 AI
security validation demonstrated proof-of-concept, with adversarial test
harness and measured results across three independent runs"

**Add after that:**

> ; 23.6 AI governance control gate demonstrated proof-of-concept, using
> measured Exhibit 23.5 data as evaluation input

---

## 3. Exhibit 24 cover pages — two additions

**(a) In the "Contents" list**, add after the 23.5 entry:

> 23.6 AI Governance Control Gate: Demonstrated Proof-of-Concept.
> Self-built pipeline evaluating candidate releases against a
> pre-deployment gate, with change control and evidence retention,
> operationalizing three of the five control domains specified at 24.4.

**(b) In the "Note on the technical designs described" section**, add
after the existing sentences about 23.5 and 24.2, Part C:

> Exhibit 23.6 similarly supplements Exhibit 24.4 with a demonstrated,
> measured proof-of-concept of three of that specification's five control
> domains (the pre-deployment evaluation gate, change control, and
> evidence retention and traceability). It does not convert the remaining
> two domains — post-deployment monitoring/drift detection and control
> mapping/consolidation — into completed, measured work.

---

## 4. Exhibit 24.5 — Declaration — new paragraph 13

If you've applied both prior edits, your declaration now ends its numbered
content at paragraph 12. **Insert a new paragraph 13** before the closing
perjury statement:

> 13. I subsequently built the governance pipeline and conducted the
> evaluation runs described at Exhibit 23.6, on September 24, 2026. Two of
> the three candidate releases evaluated used the actual measured
> adversarial leak rates from Exhibit 23.5 as evaluation input; the third
> was fabricated for this demonstration, as stated in that exhibit. The
> system and results described there are my own work, conducted
> independently on my own equipment and unconnected to any employer
> engagement.

---

## Where things stand after this edit

With all three proof-of-concept exhibits applied (23.5, 24.2 Part C, and
23.6), the petition now demonstrates work across all three endeavor
components:

- Component One (test automation): one of four specified modules demonstrated
- Component Two (security validation): two of six taxonomy categories demonstrated
- Component Three (governance): three of five control domains demonstrated

None of the three components is fully demonstrated end-to-end — each still
has prospective elements — but each now has at least one genuinely
demonstrated, measured piece rather than resting entirely on specification.
That is a materially different evidentiary posture than the petition had
before this round of work, and is likely sufficient without pursuing
further POCs unless you specifically want to close a particular remaining
gap.
