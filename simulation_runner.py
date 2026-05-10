from __future__ import annotations

import argparse
import json

from property_initializer import create_demo_market
from transaction_engine import run_market_round


def summarize_state(state) -> dict:
    return {
        "round": state.round_index,
        "agents": len(state.agents),
        "properties": len(state.properties),
        "available_properties": len(state.available_properties()),
        "transactions": [
            {
                "round": item.round_index,
                "buyer_id": item.buyer_id,
                "seller_id": item.seller_id,
                "property_id": item.property_id,
                "price": item.price,
            }
            for item in state.transactions
        ],
    }


def run_simulation(rounds: int = 1, seed: int = 42) -> dict:
    state = create_demo_market(seed)
    round_summaries = [run_market_round(state) for _ in range(max(0, int(rounds)))]
    return {
        "ok": True,
        "mode": "public_demo",
        "seed": int(seed),
        "rounds": int(rounds),
        "round_summaries": round_summaries,
        "summary": summarize_state(state),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the Atlas Market Engine public demo.")
    parser.add_argument("--rounds", type=int, default=1)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    print(json.dumps(run_simulation(rounds=args.rounds, seed=args.seed), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
