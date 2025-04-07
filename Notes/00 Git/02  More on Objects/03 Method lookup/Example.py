#Notes
#PolyMorphism
#   -Poly means many
#   -morph means many forms

#Method lookup:
#   -Form of polymorphism
#   -if a subclass doesnt have a method, the python interpreter will look at the superclass to see if it has the method 

class Shape:
    def __init__(self, Length ,Width):
        self.length = Length
        self.width = Width
        
    def draw(self):
        for _ in range(self.width):
            print("* " * self.length)
            print()

class Rectangle(Shape):
    
    def __init__(self, length, width):
        super().__init__(length, width)

    #Note we are not putting a draw method in class

class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side)

    #No draw method

class Triangle(Shape):
    
    def __init__(self, side):
        super().__init__(side, side)

    def draw(self):
        for i in range(self.width):
            print("* " * (self.width-i))

r = Rectangle(10, 5)
s = Square(3)
t = Triangle(6)

r.draw()
s.draw()
t.draw()
