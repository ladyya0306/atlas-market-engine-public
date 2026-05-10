from __future__ import annotations

from models import Agent


def estimate_monthly_payment(price: float, down_payment_ratio: float = 0.30) -> float:
    loan = max(0.0, price * (1.0 - down_payment_ratio))
    return loan * 0.0048


def can_afford(agent: Agent, price: float, down_payment_ratio: float = 0.30) -> bool:
    down_payment = price * down_payment_ratio
    monthly_payment = estimate_monthly_payment(price, down_payment_ratio)
    return agent.cash >= down_payment and monthly_payment <= agent.monthly_income * 0.55
