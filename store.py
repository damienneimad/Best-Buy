from __future__ import annotations

from typing import Iterable, List, Tuple

from products import Product


class Store:
    """Collection of products available for sale."""

    def __init__(self, products: Iterable[Product] | None = None) -> None:
        self.products: List[Product] = list(products) if products else []

    # ---- product management ----
    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        self.products.remove(product)

    def get_all_products(self) -> List[Product]:
        return [p for p in self.products if p.is_active()]

    def get_total_quantity(self) -> int:
        return sum(p.quantity for p in self.get_all_products())

    # ---- order processing ----
    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"{product.name} is not sold in this store")
            total += product.buy(quantity)
        return total

    # ---- magic methods ----
    def __contains__(self, product: Product) -> bool:
        return product in self.products

    def __add__(self, other: "Store") -> "Store":
        return Store(self.products + other.products)
