from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("roar")

class cow(Animal):
    def make_sound(self):
        print("moo")

l1 = cow()
l1.make_sound()

l2 = Lion()
l2.make_sound()