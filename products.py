class Product:
    """This class is a blueprint for all products that are sold at best buy store. It holds
    name, price, quantity and availability in stock."""

    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError(
                "Invalid product details: Name must be non-empty, price and quantity"
                "must be non-negative.")

        self.name = name
        self._price = price
        self.quantity = quantity
        self.active = quantity > 0
        self.promotion = None

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be non-negative.")
        self._price = value


    def __gt__(self, other):
        """Compares prices of two products"""
        if isinstance(other, Product):
            return self.price > other.price
        return NotImplemented

    def get_quantity(self):
        """returns the quantity of a product in the stock"""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets a new value for the quantity of an item. If a product is out of stock and
        because of this the quantity is 0 this function deactivates the product"""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """This function gets and returns a value for the question
        if a product is available."""
        return self.active

    def activate(self):
        """The function change the product status to active."""
        self.active = True

    def deactivate(self):
        """The function changes the product status to inactive."""
        self.active = False

    def show(self):
        """This function returns a f string with information about the product price
        and product quantity in stock and if product is in promotion."""
        promo_str = f" (Promotion: {self.promotion})" if self.promotion else ""
        return f"{self.name}, Price: ${self._price}, Quantity: {self.quantity}{promo_str}"

    def __str__(self):
        return self.show()


    def buy(self, quantity):
        """This function checks if enough items of product are in stock to buy it and can
        raise a ValueError in case it is not enough in stock.
        It returns the total of the cart as a float"""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self._price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion




class NonStockedProduct(Product):
    """A child product class that doesn't require stock tracking like ebooks or licences."""

    def __init__(self, name, price, active=True):
        super().__init__(name, price, quantity=0)
        self._active = active

    def set_quantity(self, quantity):
        """Override to prevent changing quantity."""
        # Non-stocked products get per default quantity 0 and should not be changed.
        pass

    def is_active(self):
        """active status of non-physical products should always be true. But deactivation by
        shop owner is possible if needed
        """
        return self._active

    def buy(self, quantity):
        # Always allow purchase of a positive amount, but don't change stock quantity
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0.")
        if not self._active:
            raise ValueError("product is not active!")
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        return total_price


    def show(self):
        promotion_text = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited{promotion_text}"

    def __str__(self):
        return self.show()


class LimitedProduct(Product):
    """A product child class that can only be bought in limited quantities per order,
    independent to the amount in stock."""

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of this item per order.")

        return super().buy(quantity)

    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity} (Limit: {self.maximum} per order)"


    def __str__(self):
        return self.show()


if __name__ == "__main__":
    """This function initializes product instances, and runs the class methods for
    demonstration at the moment. It simulates a purchase,  restock of items and
    can check the status of a product."""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())
