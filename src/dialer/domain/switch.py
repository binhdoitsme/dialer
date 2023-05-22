from typing import Optional
from .operator import Operator


class Switch:
    def __init__(self):
        self._operators: dict[str, Operator] = {}

    def add_pricing(self, operator_name: str, prefix: str, price: float):
        if operator_name not in self._operators:
            self._operators[operator_name] = Operator(operator_name)
        self._operators[operator_name].add_pricing(prefix, price)

    def route(self, phone_number: str) -> Optional[tuple[str, float]]:
        best_operator: Optional[str] = None
        best_price: float = float("inf")
        for name, operator in self._operators.items():
            price = operator.pricing_for(phone_number)
            if price is None:
                continue
            if price < best_price:
                best_operator = name
                best_price = price
        if best_operator is not None:
            return best_operator, best_price
        return None
