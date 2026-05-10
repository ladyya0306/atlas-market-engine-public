from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from simulation_runner import run_simulation


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the public demo smoke test.")
    parser.add_argument("--rounds", type=int, default=1)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    payload = run_simulation(rounds=args.rounds, seed=args.seed)
    assert payload["ok"] is True
    assert payload["summary"]["agents"] > 0
    assert payload["summary"]["properties"] > 0
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
