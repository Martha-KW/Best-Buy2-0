import pytest

from products import Product
from promotions import ThirdOneFree, PercentDiscount, SecondHalfPrice
from store import Store


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


def test_third_one_free_promotion():
    """This tests if promotion 3rd one free ist working"""
    product = Product("Bose QC", price=100, quantity=10)
    promo = ThirdOneFree("Buy 2 get 1")
    product.set_promotion(promo)

    total = product.buy(3)
    assert total == 200


def test_percent_discount_promotion():
    """This tests if simple discount by percent value is working"""
    product = Product("Testprodukt", price=200, quantity=5)
    promo = PercentDiscount("30% off", percent=30)
    product.set_promotion(promo)

    total = product.buy(2)
    expected = (200 * 0.7) * 2
    assert total == expected


def test_second_half_price_promotion():
    """This tests if you can buy a second product at half price if promoted """
    product = Product("Testprodukt", price=100, quantity=10)
    promo = SecondHalfPrice("Second item half price")
    product.set_promotion(promo)

    total = product.buy(2)
    expected = 100 + 50
    assert total == expected

    total = product.buy(3)
    expected = 100 + 50 + 100
    assert total == expected


def test_magic_methods():
    """Tests for the bonus section of magic methods"""

    mac = Product("MacBook Air M2", price=1450, quantity=100)
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    store = Store([mac, bose])

    # Test str method
    assert str(mac) == "MacBook Air M2, Price: $1450, Quantity: 100"

    # Test comparison
    assert mac > bose
    assert not bose > mac

    # Test in operator
    assert mac in store
    assert pixel not in store

    # Test price setter validation
    with pytest.raises(ValueError):
        mac.price = -50
