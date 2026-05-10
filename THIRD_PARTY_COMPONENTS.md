# Third-Party Components and Upstream Lineage

Date: 2026-05-10

## Current Project License

- Main license: PolyForm Noncommercial License 1.0.0.
- License file: [LICENSE](LICENSE).
- Commercial use requires separate written authorization.

## Upstream Lineage

| Component | Role in this project | Original license | Local attribution |
| --- | --- | --- | --- |
| CAMEL-AI OASIS | Historical inspiration and partial lineage for multi-agent simulation concepts | Apache License 2.0 | [NOTICE](NOTICE), [ATTRIBUTION.md](ATTRIBUTION.md), [licenses/Apache-2.0.txt](licenses/Apache-2.0.txt) |

This repository is not the official OASIS repository and does not imply endorsement by CAMEL-AI or OASIS maintainers.

## Runtime Dependencies

Dependencies are installed through normal package managers and are not vendored as project-owned source code.

| Dependency | Usage | Declared in |
| --- | --- | --- |
| FastAPI, Uvicorn | Local API service and Web dashboard | [requirements.txt](requirements.txt) |
| PyYAML | Optional configuration reading | [requirements.txt](requirements.txt) |
| pytest | Public package tests | [requirements.txt](requirements.txt) |
