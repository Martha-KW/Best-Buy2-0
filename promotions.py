from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Calculate discounted price for a given product and quantity"""
        pass

    def __str__(self):
        return self.name


class PercentDiscount(Promotion):
    """a child class for classic percentage discount"""
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """a child class that allows to apply the discount only to the second product"""
    def apply_promotion(self, product, quantity):
        half_items = quantity // 2
        full_items = quantity - half_items
        return product.price * (full_items + half_items * 0.5)


class ThirdOneFree(Promotion):
    """a child class to add the third product for free"""
    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        paid_items = quantity - free_items
        return product.price * paid_items
