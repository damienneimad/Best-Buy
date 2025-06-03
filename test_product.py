import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount

def test_buy_reduces_quantity():
    p = Product('Test', price=10, quantity=5)
    p.buy(2)
    assert p.quantity == 3

def test_buy_with_promotion():
    p = Product('Test', price=100, quantity=5)
    p.set_promotion(PercentDiscount('half', percent=50))
    total = p.buy(2)
    assert pytest.approx(total) == 100

def test_non_stocked():
    p = NonStockedProduct('Digital', price=15)
    total = p.buy(3)
    assert total == 45

def test_limited_product_limit():
    lp = LimitedProduct('Limited', price=10, quantity=10, maximum=2)
    with pytest.raises(ValueError):
        lp.buy(3)
