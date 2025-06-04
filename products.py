from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


class Product:
    """Base product sold in the store."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        if not name:
            raise ValueError("name cannot be empty")
        if price < 0:
            raise ValueError("price cannot be negative")
        if quantity < 0:
            raise ValueError("quantity cannot be negative")

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True
        self._promotion: Optional[Promotion] = None

    # ---- properties ----
    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("price cannot be negative")
        self._price = value

    @property
    def quantity(self) -> int:
        return self._quantity

    def set_quantity(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("quantity cannot be negative")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()

    # ---- activation ----
    def is_active(self) -> bool:
        return self._active

    def activate(self) -> None:
        self._active = True

    def deactivate(self) -> None:
        self._active = False

    # ---- promotion ----
    def set_promotion(self, promotion: Optional[Promotion]) -> None:
        self._promotion = promotion

    def get_promotion(self) -> Optional[Promotion]:
        return self._promotion

    # ---- operations ----
    def show(self) -> str:
        return f"{self.name}, Price: ${self.price} Quantity:{self.quantity}"

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if quantity > self.quantity:
            raise ValueError("not enough quantity in stock")
        total = self.price * quantity
        if self._promotion:
            total = self._promotion.apply_promotion(self, quantity)
        self.set_quantity(self.quantity - quantity)
        return total

    # ---- magic methods ----
    def __str__(self) -> str:
        return self.show()

    def __gt__(self, other: "Product") -> bool:
        return self.price > other.price


class NonStockedProduct(Product):
    """Product that does not manage quantity."""

    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int) -> None:  # override
        # Non-stocked products always have quantity of 0 but are active
        if quantity != 0:
            raise ValueError("NonStockedProduct quantity must stay 0")

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)
        return self.price * quantity


class LimitedProduct(Product):
    """Product that has a purchase limit per order."""

    def __init__(self, name: str, price: float, quantity: int, maximum: int) -> None:
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("maximum must be positive")
        self._maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self._maximum:
            raise ValueError(f"Cannot buy more than {self._maximum} items")
        return super().buy(quantity)


# Circular import prevention
from promotions import Promotion  # noqa: E402
