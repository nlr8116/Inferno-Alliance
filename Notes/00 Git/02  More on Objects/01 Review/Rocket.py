
class Rocket:
    #class variables
    has_engine = True
    Max_Capacity = 10000
    Min_Capacity = 0
    allowed_brands = ["NASA", "Space X"]

    def __int__(self, name, brand, has_crew = False):
        self.name = name
        self.brand = brand
        self.has_crew = has_crew
        self._crew_size = -10
        self.destination = ""

    @property
    def crew_size (self):
        return self._crew_size
    
    @crew_size.setter
    def crew_size(self, new_crew):
        if new_crew in range(Rocket.Min_Capacity, Rocket.Max_Capacity +1):
                self._crew_size = new_crew
    
    @property
    def brand (self):
        return self._brand
    
    @brand.setter
    def brand(self, brand_name):
        if brand_name in Rocket.allowed_brands:
            self._brand = brand_name
        else:
            self._brand = ""
    
    @classmethod
    def add_brand(cls, new_brand):
        cls.allowed_brands.append(new_brand)
    
    @staticmethod
    def reset_brands():
        Rocket.allowed_brands = []

    def __str__(self):
        return f"{self.brand} -- {self._crew_size}"
    
