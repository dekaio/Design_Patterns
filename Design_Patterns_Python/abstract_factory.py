import abc


# An abstract factory groups different class instantiations together
# Objective is to group classes together
class Product(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

class Fruit(Product):

    def __init__(self):
        pass


class Vegetable(Product):

    def __init__(self):
        pass


class AppleFruit(Fruit):

    def __init__(self):
        print("Prepared Apple fruit")


class TomatoVegetable(Vegetable):

    def __init__(self):
        print("Prepared Tomato vegetable")


class KiwiFruit(Fruit):

    def __init__(self):
        print("Prepared Kiwi fruit")


class BrocoliVegetable(Vegetable):

    def __init__(self):
        print("Prepared Brocoli fruit")


class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_product_fruit(self):
        pass

    @abc.abstractmethod
    def get_product_vegetable(self):
        pass


class IndigenousFactory(AbstractFactory):
    def get_product_fruit(self):
        return AppleFruit()

    def get_product_vegetable(self):
        return TomatoVegetable()


class ForeignFactory(AbstractFactory):

    def get_product_fruit(self):
        return KiwiFruit()

    def get_product_vegetable(self):
        return TomatoVegetable()


factory = IndigenousFactory()
factory.get_product_fruit()
factory.get_product_vegetable()
