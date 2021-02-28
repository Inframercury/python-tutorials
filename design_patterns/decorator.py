from abc import ABC, abstractmethod


class Creature(ABC):

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass

class Animal(Creature):

    def make_noise(self):
        print("WOOO!")

    def move(self):
        print("I walk forward")

    def feed(self):
        print("I eat grass")

