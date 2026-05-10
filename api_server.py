from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from property_initializer import create_demo_market
from simulation_runner import summarize_state
from transaction_engine import run_market_round


app = FastAPI(title="Atlas Market Engine Public Demo", version="1.0.0")
_state = create_demo_market(seed=42)
_root = Path(__file__).resolve().parent
_web_root = _root / "web"

if _web_root.exists():
    app.mount("/web", StaticFiles(directory=str(_web_root)), name="web")


@app.get("/")
def index():
    return FileResponse(_web_root / "index.html")


@app.get("/health")
def health() -> dict:
    return {"ok": True, "mode": "public_demo"}


@app.post("/start")
def start(payload: dict | None = None) -> dict:
    global _state
    payload = payload or {}
    seed = int(payload.get("seed", 42))
    _state = create_demo_market(seed=seed)
    return {"ok": True, "state": summarize_state(_state)}


@app.post("/step")
def step() -> dict:
    round_summary = run_market_round(_state)
    return {"ok": True, "round": round_summary, "state": summarize_state(_state)}


@app.get("/status")
def status() -> dict:
    return {"ok": True, "state": summarize_state(_state)}


@app.get("/controls")
def controls() -> dict:
    return {
        "ok": True,
        "controls": [
            {"key": "seed", "type": "integer", "default": 42},
            {"key": "rounds", "type": "integer", "default": 1},
        ],
    }


@app.get("/presets")
def presets() -> dict:
    return {
        "ok": True,
        "presets": [
            {"id": "starter_demo", "name": "Starter demo"},
            {"id": "balanced_demo", "name": "Balanced demo"},
        ],
    }


@app.post("/presets/apply")
def apply_preset(payload: dict | None = None) -> dict:
    seed = 42 if not payload else int(payload.get("seed", 42))
    return start({"seed": seed})


@app.get("/report/final")
def final_report() -> dict:
    return {"ok": True, "summary": summarize_state(_state)}


@app.get("/report/final/view")
def final_report_view() -> dict:
    return final_report()
