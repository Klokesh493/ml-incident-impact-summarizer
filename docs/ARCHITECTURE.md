# Ml Incident Impact Summarizer architecture

Summarizes ML incident blast radius from model, endpoint, feature, and customer segment data.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
