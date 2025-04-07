class Animal:
    def __init__(self):
        """Makes an animal or doesnint because its abstract"""

    def communiate (self):
        raise NotImplementedError("Need to implement communicate")
    
class bird(Animal):
    def __init__(self):
        """Bird stuff"""

    def communiate(self):
        print("Chirp Squawk, cocka doodle do, Tweet, KaKaw")

A = Animal()
b = bird()
b.communiate()