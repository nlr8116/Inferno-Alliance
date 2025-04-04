#Notes
#PolyMorphism
#   -Poly means many
#   -morph means many forms

#Method lookup:
#   -Form of polymorphism
#   -if a subclass doesnt have a method, the python interpreter will look at the superclass to see if it has the method 

class Shape:
    def __int__(self, Length ,Width):
        self.length = Length
        self.width = Width
        
    def draw(self):
        for _ in range(self.width):
            print("* " * self.length)
            print()

class Triangle(Shape):
    pass

class Rectangle(Shape):
    pass

class Square(Rectangle):
    pass