import products


class Store:
    """
    This class simulates a store that manages a collection of products.
    It adds/removes products, checks the inventory,
    and coordinates orders.
    """

    def __init__(self, products):
        """Initializes the store with a list of products."""
        self.products = products

    def add_product(self, product):
        """Adds a product to the inventory."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the inventory if possible."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """Returns the total of how many products are in stock of the store."""
        return sum(product.get_quantity()
                   for product in self.get_all_products())

    def get_all_products(self):
        """Returns all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        This gets a list of tuples consisting of two items: product and quantity. It buys the
        products and returns the total price of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


if __name__ == "__main__":
    product_list = [
        products.Product(
            "MacBook Air M2", price=1450, quantity=100), products.Product(
            "Bose QuietComfort Earbuds", price=250, quantity=500), products.Product(
                "Google Pixel 7", price=500, quantity=250), ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))
