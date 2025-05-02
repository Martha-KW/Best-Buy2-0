from products import Product, NonStockedProduct, LimitedProduct
from promotions import Promotion


class ShoppingCart:
    """This class initializes a shopping cart to be able to sum the amount of the goods"""
    def __init__(self):
        self.items = {}  # key = Product, value = quantity

    def add_product(self, product, quantity):
        if product not in self.items:
            self.items[product] = 0
        self.items[product] += quantity

    def get_total(self):
        total = 0
        for product, quantity in self.items.items():
            if product.promotion:
                total += product.promotion.apply_promotion(product, quantity)
            else:
                total += product.price * quantity
        return total

    def checkout(self):
        """buys the products from cart an empties cart after purchase."""
        total = 0
        for product, quantity in self.items.items():
            # here is the price calculation with or without promotion
            if product.promotion:
                total += product.promotion.apply_promotion(product, quantity)
            else:
                total += product.price * quantity


            if not isinstance(product, NonStockedProduct):
                product.buy(quantity)

        self.items.clear()
        return total

    def show_cart(self):
        for product, quantity in self.items.items():
            print(f"{product.name} x {quantity}")
