from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


AgentRole = Literal["buyer", "seller", "observer"]


@dataclass
class Agent:
    id: int
    name: str
    role: AgentRole
    cash: float
    monthly_income: float
    preference_zone: str
    max_budget: float
    owned_property_ids: list[int] = field(default_factory=list)


@dataclass
class Property:
    id: int
    zone: str
    area_sqm: float
    list_price: float
    owner_id: int | None = None
    status: Literal["available", "sold"] = "available"


@dataclass
class Transaction:
    round_index: int
    buyer_id: int
    seller_id: int
    property_id: int
    price: float


@dataclass
class MarketState:
    round_index: int
    agents: list[Agent]
    properties: list[Property]
    transactions: list[Transaction] = field(default_factory=list)

    def available_properties(self) -> list[Property]:
        return [item for item in self.properties if item.status == "available"]
