from abc import ABCMeta, abstractclassmethod 

class Animal(metaclass = ABCMeta):
    def __init(self):
        """s"""

    def communicate(self):
        """left for subclass"""

class Bird(Animal):
    def __init__(self):
        """Bird Stuff"""
    def communicate(self):
        print("Put the pollu chirps biayureifff")

a = Animal()
b = Bird()
b.communicate()