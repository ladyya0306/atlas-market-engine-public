from __future__ import annotations

import random

from models import Agent, MarketState, Property


def create_demo_market(seed: int = 42) -> MarketState:
    """Create a small deterministic market for public demos."""

    rng = random.Random(seed)
    zones = ["core", "subcore", "outer"]
    agents: list[Agent] = []
    properties: list[Property] = []

    for idx in range(1, 7):
        role = "seller" if idx in {1, 2, 3} else "buyer"
        zone = zones[(idx + seed) % len(zones)]
        cash = 260_000 + rng.randint(0, 160_000)
        income = 18_000 + rng.randint(0, 12_000)
        budget = cash * 3.2 + income * 48
        agents.append(
            Agent(
                id=idx,
                name=f"agent-{idx}",
                role=role,
                cash=float(cash),
                monthly_income=float(income),
                preference_zone=zone,
                max_budget=float(budget),
            )
        )

    for idx in range(1, 5):
        owner_id = idx if idx <= 3 else None
        zone = zones[(idx + seed + 1) % len(zones)]
        price = 780_000 + rng.randint(0, 520_000)
        properties.append(
            Property(
                id=idx,
                zone=zone,
                area_sqm=float(68 + idx * 8),
                list_price=float(price),
                owner_id=owner_id,
            )
        )
        if owner_id:
            agents[owner_id - 1].owned_property_ids.append(idx)

    return MarketState(round_index=0, agents=agents, properties=properties)
