
class Rocket:
    #class variables
    has_engine = True
    Max_Capacity = 10000

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
    def crew_size(self, new_crew, Max_Capacity = Max_Capacity):
        if new_crew < 0:
            self._crew_size = 0
        if new_crew > Max_Capacity:
            self._crew_size = Max_Capacity
