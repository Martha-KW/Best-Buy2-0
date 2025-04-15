class Product:
    """This class is a blueprint for all products that are sold at best buy store. It holds
    name, price, quantity and availability in stock."""

    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError(
                "Invalid product details: Name must be non-empty, price and quantity"
                "must be non-negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

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
        "This function gets and returns a value for the question if a product is available."
        return self.active

    def activate(self):
        """The function change the product status to active."""
        self.active = True

    def deactivate(self):
        """The function changes the product status to inactive."""
        self.active = False

    def show(self):
        """This function returns a f string with information about the product price
        and product quantity in stock."""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """This function checks if enough items of product are in stock to buy it and can
        raise a ValueError in case it is not enough in stock.
        It returns the total of the cart as a float"""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


# Test cases
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
