# Project Modification Log

Date: 2026-05-10

Atlas Market Engine started from public multi-agent simulation ideas and has
been reshaped into a real-estate market simulation project. This public
repository now contains only a lightweight noncommercial demo.

## Public Demo Work

| Area | Files | Public work |
| --- | --- | --- |
| Data model | [models.py](models.py), [property_initializer.py](property_initializer.py) | Defines small demo agents, properties, transactions, and market state. |
| Behavior flow | [agent_behavior.py](agent_behavior.py) | Provides simple behavior selection for the public demo. |
| Rule layer | [mortgage_system.py](mortgage_system.py), [transaction_engine.py](transaction_engine.py) | Checks affordability, records transactions, and updates property state. |
| Runtime | [simulation_runner.py](simulation_runner.py), [real_estate_demo_v2_1.py](real_estate_demo_v2_1.py) | Provides CLI execution for the public demo. |
| API and Web | [api_server.py](api_server.py), [web/](web/) | Provides a local FastAPI service and browser dashboard. |
| Packaging | [README.md](README.md), [docs/](docs/), [tests/test_public_package.py](tests/test_public_package.py) | Documents the public scope, license, attribution, and smoke-test path. |

## 2026-05-10 Public Hardening

- Removed release-production assets and presentation files from the public tree.
- Removed reusable high-value decision-template material from the public tree.
- Replaced commercial-scale configuration with a toy public-demo configuration.
- Reduced the public repository to a small runnable demo with CLI, API, Web, and tests.
- Prepared the repository to be republished as a clean single-history public branch.
