from math import pi
class shape:
    def __init__ (self, area, perimeter, coloure):
        self.area = area
        self.perimeter = perimeter 
        self.coloure = coloure 
    def area (self):
        pass 
class circle:
    def __init__ (self, radius):
        self.radius = radius  
    def area(self, radius):
        return pi * radius ** 2
    def perimeter(self, radius):
        return 2 * pi * radius 