# Atlas Market Engine

## 项目简介 / Overview

Atlas Market Engine 是一个房地产市场多智能体仿真演示项目。当前公开仓库提供一个轻量、可复现、非商业许可的演示内核，用于展示买方、卖方、房源、支付能力校验、成交记录和 Web 控制台的基本工作流。

Atlas Market Engine is a multi-agent real-estate market simulation demo. This public repository contains a lightweight, reproducible, noncommercial demo core that shows buyers, sellers, properties, affordability checks, transaction records, and a browser dashboard.

## 当前公开版定位 / Public Edition Scope

本仓库用于品牌展示、社区评估、教学演示和非商业研究原型。它不是商业版完整交付，也不包含未公开实验素材、商业参数包、客户数据接口或可复用的高价值决策模板。

This repository is intended for brand presence, community evaluation, teaching demos, and noncommercial research prototypes. It is not the complete commercial edition and does not include private experiment assets, commercial parameter packs, client-data adapters, or high-value reusable decision templates.

## 快速开始 / Quick Start

环境要求：

Requirements:

- Python 3.10+
- Windows, macOS, or Linux

安装依赖：

Install dependencies:

```bash
pip install -r requirements.txt
```

运行最短检查：

Run the shortest check:

```bash
python scripts/public_smoke_test.py --rounds 1 --seed 42
```

直接运行演示：

Run the demo directly:

```bash
python simulation_runner.py --rounds 2 --seed 42
```

启动 Web 控制台：

Start the web dashboard:

```bash
python -m uvicorn api_server:app --reload
```

Open:

```text
http://127.0.0.1:8000/
```

Windows 用户也可以使用：

Windows users can also run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start_web_ui.ps1
```

## API 概览 / API Overview

- `GET /health`
- `POST /start`
- `POST /step`
- `GET /status`
- `GET /controls`
- `GET /presets`
- `POST /presets/apply`
- `GET /report/final`
- `GET /report/final/view`
- `GET /`
- `GET /web/*`

## 项目结构 / Project Layout

- `models.py`: public demo data models.
- `property_initializer.py`: deterministic demo-market setup.
- `agent_behavior.py`: simple public-demo behavior selection.
- `mortgage_system.py`: affordability checks.
- `transaction_engine.py`: settlement and state updates.
- `simulation_runner.py`: CLI simulation entry.
- `api_server.py`: FastAPI service and Web dashboard entry.
- `web/`: browser dashboard assets.
- `scripts/`: public smoke test and startup helper.
- `docs/`: public-facing documentation.

## 测试 / Tests

```bash
python -m pytest tests/test_public_package.py -q
```

## 许可证 / License

本仓库采用 PolyForm Noncommercial License 1.0.0。详见 [LICENSE](LICENSE)。

This repository is released under the PolyForm Noncommercial License 1.0.0. See [LICENSE](LICENSE).

在许可证允许的非商业范围内，你可以使用、学习、修改和分享本项目。商业部署、付费服务、转售、商业集成或生产型商业使用需要另行取得书面授权。

You may use, study, modify, and share the project for permitted noncommercial purposes under the license terms. Commercial deployment, paid service use, resale, commercial integration, or production business use requires separate written permission.

## 归属说明 / Attribution

Atlas Market Engine 受到 CAMEL-AI OASIS 相关公开工作的启发，并包含从相关开源思想演化而来的部分工程边界说明。本仓库不是 CAMEL-AI 或 OASIS 的官方发布。

Atlas Market Engine was inspired by CAMEL-AI OASIS-related public work and includes engineering-boundary ideas evolved from related open-source material. This repository is not an official CAMEL-AI or OASIS release.

Relevant files:

- [NOTICE](NOTICE)
- [ATTRIBUTION.md](ATTRIBUTION.md)
- [THIRD_PARTY_COMPONENTS.md](THIRD_PARTY_COMPONENTS.md)
- [MODIFICATION_LOG.md](MODIFICATION_LOG.md)
- [licenses/Apache-2.0.txt](licenses/Apache-2.0.txt)
