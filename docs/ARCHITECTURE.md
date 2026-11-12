# Ml Incident Impact Summarizer architecture

Summarizes ML incident blast radius from model, endpoint, feature, and customer segment data.

```mermaid
flowchart LR
    N0["sample_ml_incidents.csv"]
    N1["ml_impact.py"]
    N2["summarize"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
