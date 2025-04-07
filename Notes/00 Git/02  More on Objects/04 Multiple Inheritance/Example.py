#Multiple inheritance occurs when a class has at least two direct super classes 

#Single inheritence multiple times is not multiple inheritence

class Bread:
    def __init__(self, flour_type, is_moldy):
        self.flour_type = flour_type
        self.is_moldy = is_moldy

    def __str__(self):
        return f"{self.flour_type = }\n{self.is_moldy=}"
    

class SaleItem:
    def __init__(self, price):
        self.price = price

    def __str__(self):
        return f"{self.price=}"


class HamburgerBun(Bread, SaleItem):
    def __init__(self):
        Bread.__init__(self, "Wheat", True)
        SaleItem.__init__(self, 101.99)

    def __str__(self):
        return f"Hamburger Bun: " + Bread.__str__(self) + SaleItem.__str__(self)

bun = HamburgerBun()
print(bun)