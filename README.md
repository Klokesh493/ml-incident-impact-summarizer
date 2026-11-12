# ML Incident Impact Summarizer

Summarizes ML incident blast radius from model, endpoint, feature, and customer segment data.

Focus: AI/ML platform incident response.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 ml_impact.py sample_ml_incidents.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

When several models are affected, responders need to estimate endpoint coverage and customer impact from the incident records they have.

## Project walkthrough

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

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 ml_impact.py sample_ml_incidents.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.

## Development and security

See the [developer setup, tool roles, and security checks](docs/DEVELOPMENT.md).

[Local check results](reports/devsecops.md)

## Runbook

[Run, verify, and troubleshoot this project](docs/RUNBOOK.md)
