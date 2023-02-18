# used to extend functionality of a class
# No emphasis on families

import abc


class Product(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def get_name(self):
        pass
class Fruit(Product):

    def __init__(self):
        pass
    def get_name(self):
        print("Fruit!")

class Vegetable(Product):

    def __init__(self):
        pass

    def get_name(self):
        print("Vegetable!")


class AppleFruit(Fruit):

    def __init__(self):
        print("Prepared Apple fruit")

    def get_name(self):
        print("Apple Fruit!")
class TomatoVegetable(Vegetable):

    def __init__(self):
        print("Prepared Tomato vegetable")

    def get_name(self):
        print("Tomato Vegetable!")

class KiwiFruit(Fruit):

    def __init__(self):
        print("Prepared Kiwi fruit")

    def get_name(self):
        print("Kiwi Fruit")

class BrocoliVegetable(Vegetable):

    def __init__(self):
        print("Prepared Brocoli fruit")

    def get_name(self):
        print("Brocoli vegetable")

class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_product(self):
        pass
    def slice_product(self,product:Product):
        pass

class FruitFactory(AbstractFactory):

    def get_product(self):
        return AppleFruit()

    def slice_product(self, product:Product):
        product.get_name()
        print("Sliced this fruit into pieces")

class VegetableFactory(AbstractFactory):

    def get_product(self):
        return BrocoliVegetable()

    def slice_product(self, product:Product):
        product.get_name()
        print("Sliced this fruit into pieces")

fruit_factory = FruitFactory()
fruit = fruit_factory.get_product()
fruit_factory.slice_product(fruit)
