"""
Used when creating a new object may require more resources than we have or available versus just making a copy in
the memory
Decide if shallow copy (new compound object plus references to the objects in the original) or deep copy (new compound
object plus copy of the objects found in the original) is required
"""
import abc


class IPrototype(metaclass=abc.ABCMeta):

"Making this abstract static method made all the difference. Just making it abstract doesn't seem to have any effect"
    @abc.abstractstaticmethod
    def clone(self):
        pass

class Human(IPrototype):

    def __init__(self, name:str, height:float, weight:int):
        self.name = name
        self.height = height
        self.weight = weight

    def clone(self):
        return type(self)(
            self.name,
            self.height,
            self.weight
        )

human = Human("Poppy", 5.5, 55)
clone = human.clone()
print(id(human), id(clone))