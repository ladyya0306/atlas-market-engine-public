from __future__ import annotations

from models import Agent, MarketState, Property


def choose_property(agent: Agent, state: MarketState) -> Property | None:
    """Choose a visible property with simple public-demo scoring."""

    candidates = state.available_properties()
    if not candidates:
        return None
    affordable = [item for item in candidates if item.list_price <= agent.max_budget]
    pool = affordable or candidates
    return sorted(
        pool,
        key=lambda item: (
            0 if item.zone == agent.preference_zone else 1,
            abs(item.list_price - min(agent.max_budget, item.list_price)),
            item.id,
        ),
    )[0]


def offer_price(agent: Agent, prop: Property, round_index: int) -> float:
    pressure = min(0.04, round_index * 0.01)
    ceiling = min(agent.max_budget, prop.list_price * (0.95 + pressure))
    return round(max(prop.list_price * 0.88, ceiling), 2)


def seller_accepts(prop: Property, offer: float) -> bool:
    return offer >= prop.list_price * 0.92
