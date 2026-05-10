from __future__ import annotations

from agent_behavior import choose_property, offer_price, seller_accepts
from models import MarketState, Transaction
from mortgage_system import can_afford


def run_market_round(state: MarketState) -> dict:
    state.round_index += 1
    events: list[dict] = []

    buyers = [agent for agent in state.agents if agent.role == "buyer"]
    for buyer in buyers:
        prop = choose_property(buyer, state)
        if prop is None or prop.owner_id is None:
            events.append({"type": "no_match", "buyer_id": buyer.id})
            continue

        offer = offer_price(buyer, prop, state.round_index)
        if not can_afford(buyer, offer):
            events.append({"type": "affordability_rejected", "buyer_id": buyer.id, "property_id": prop.id})
            continue

        if not seller_accepts(prop, offer):
            events.append({"type": "offer_rejected", "buyer_id": buyer.id, "property_id": prop.id, "offer": offer})
            continue

        seller_id = int(prop.owner_id)
        prop.status = "sold"
        prop.owner_id = buyer.id
        buyer.owned_property_ids.append(prop.id)
        state.transactions.append(
            Transaction(
                round_index=state.round_index,
                buyer_id=buyer.id,
                seller_id=seller_id,
                property_id=prop.id,
                price=offer,
            )
        )
        events.append(
            {
                "type": "transaction",
                "buyer_id": buyer.id,
                "seller_id": seller_id,
                "property_id": prop.id,
                "price": offer,
            }
        )

    return {
        "round": state.round_index,
        "events": events,
        "available": len(state.available_properties()),
        "transactions": len(state.transactions),
    }
