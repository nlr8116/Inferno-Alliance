class Animal(ABC):
    def __init__(self):
        """"""
    
    @abstractmethod
    def communicate(self):
        """animal communication left for subclass"""
    
class Bird(Animal):
    def __init__(self):
        """Bird things"""
    
    def communicate(self):
        print("Polly wanna cracker")

a = Animal()
b = Bird()
b.communicate(0)