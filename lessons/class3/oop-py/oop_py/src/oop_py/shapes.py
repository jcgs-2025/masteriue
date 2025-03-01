from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,base,height):
        super().__init__()
        self.base = base
        self.height = height
        
    @abstractmethod
    def area(self):
        pass
    
    def description(self):
        return f"Shape with base {self.base} and height {self.height}"

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base, height)

    def area(self):
        return self.base * self.height / 2

    def description(self):
        return f"Triangle with base {self.base} and height {self.height}"
    
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def area(self):
        return self.width * self.height

    def description(self):
        return f"Rectangle with width {self.width} and height {self.height}"