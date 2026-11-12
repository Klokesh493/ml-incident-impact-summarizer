# Ml Incident Impact Summarizer walkthrough

## Business problem

When several models are affected, responders need to estimate endpoint coverage and customer impact from the incident records they have.

## Reproduce the workflow

Run `python3 ml_impact.py sample_ml_incidents.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
{'models': 1, 'endpoints': 2, 'affected_users': 11500, 'severity': 'sev1'}
```

The sample supplies these fields. `model`, `endpoint`, `affected_users`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
