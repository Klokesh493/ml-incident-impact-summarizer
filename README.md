# ML Incident Impact Summarizer

When several models are affected, responders need to estimate endpoint coverage and customer impact from the incident records they have.

## What I built

I built a blast-radius summary that counts distinct models and endpoints, totals reported affected users, and assigns severity by user count and endpoint coverage.

## How it works

```mermaid
flowchart LR
    A["ML incident records"]
    B["Count unique models and endpoints, sum affected users"]
    C["Compare user and endpoint thresholds"]
    D["SEV1 at 10000 users or three endpoints"]
    E["SEV2 or SEV3 by user count"]
    A --> B --> C
    C --> D
    C --> E
```

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [ml_impact.py](ml_impact.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 ml_impact.py sample_ml_incidents.csv
```

The fixture reports one model, two endpoints, and 11,500 affected users, giving SEV1. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 ml_impact.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

Users are summed across rows. Deduplicate upstream if the same users can be counted in multiple records.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
