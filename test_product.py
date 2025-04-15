import pytest
from products import Product


def test_create_valid_product():
    """This tests if creating a correct product works as expected without issues"""
    p = Product("MacBook Air", price=1200, quantity=5)
    assert p.name == "MacBook Air"
    assert p.price == 1200
    assert p.quantity == 5
    assert p.active is True


def test_product_with_empty_name_raises_exception():
    """This should give an exception if the name of a new product is missing"""
    with pytest.raises(ValueError):
        Product("", price=1200, quantity=5)


def test_product_with_negative_price_raises_exception():
    """This gives an exception if shopping would cause a refund instead of increasing the
    bill of the customer to prevent financial loss """
    with pytest.raises(ValueError):
        Product("MacBook", price=-10, quantity=5)


def test_product_becomes_inactive_when_quantity_zero():
    """Customer should not see products that are out of stock so this checks if deactivation
     works to hide run out products from frontend"""
    p = Product("Pixel", price=600, quantity=1)
    p.buy(1)
    assert p.quantity == 0
    assert not p.active


def test_product_purchase_reduces_quantity_and_returns_total():
    """This tests if the stock amount is reduced correctly after a purchase"""
    p = Product("iPad", price=500, quantity=10)
    total = p.buy(3)
    assert total == 1500
    assert p.quantity == 7


def test_buying_more_than_available_raises_exception():
    """This checks if the program warns the customer that he wants to by more than available
    and interrupts the process of purchase of this item"""
    p = Product("AirPods", price=200, quantity=2)
    with pytest.raises(ValueError):
        p.buy(3)
