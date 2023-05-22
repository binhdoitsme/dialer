from typing import Optional
from dialer.util.trie import Trie


class Operator:
    def __init__(self, name: str, pricings: Optional[list[tuple[str, float]]] = None) -> None:
        self._name = name
        self._store: Trie[float] = Trie()
        if pricings is not None:
            for prefix, price in pricings:
                self._store.insert(prefix, price)
    
    def add_pricing(self, prefix: str, price: float):
        if price < 0:
            raise ValueError(f"Invalid price: {price}")
        self._store.insert(prefix, price)

    @property
    def name(self):
        return self._name
    
    def pricing_for(self, phone_number: str) -> Optional[float]:
        match = self._store.longest_match(phone_number)
        if match is not None:
            _, price = match
            return price
        return None
