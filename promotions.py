class Promotion:
    """Base class for product promotions."""

    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def apply_promotion(self, product, quantity: int) -> float:
        """Calculate the price after promotion for the given quantity."""
        raise NotImplementedError


class PercentDiscount(Promotion):
    """Percentage based discount."""

    def __init__(self, name: str, percent: float) -> None:
        super().__init__(name)
        if percent < 0 or percent > 100:
            raise ValueError("percent must be between 0 and 100")
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """Second item is sold at half price."""

    def apply_promotion(self, product, quantity: int) -> float:
        full_price_qty = quantity // 2 + quantity % 2
        half_price_qty = quantity // 2
        return product.price * full_price_qty + product.price * 0.5 * half_price_qty


class ThirdOneFree(Promotion):
    """Buy two get one free."""

    def apply_promotion(self, product, quantity: int) -> float:
        chargeable_qty = quantity - quantity // 3
        return product.price * chargeable_qty
