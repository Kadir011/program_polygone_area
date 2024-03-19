'''
Create a single function (it's important that it is only one) 
that is capable to calculate and return the area of a polygon.
- The function will receive only ONE polygon per parameter at a time.
- The supported polygons will be Triangle, Square and Rectangle.
- Prints the calculation of the area of ​​a polygon of each type.
'''
from abc import abstractmethod,ABC 

class Polygone(ABC): 
    @abstractmethod
    def area(self): 
        pass 

    @abstractmethod
    def show(self): 
        pass 

class Rectangle(Polygone): 
    def __init__(self, length, width): 
        self.length = length 
        self.width = width 

    def area(self): 
        return self.length * self.width 
    
    def show(self): 
        print(f"Rectangle Area = {self.area():.2f} cm^2") 

class Triangle(Polygone): 
    def __init__(self, base, height): 
        self.base = base
        self.height = height 

    def area(self): 
        return (self.base * self.height) / 2 
    
    def show(self): 
        print(f"Triangle Area = {self.area():.2f} cm") 

class Square(Polygone): 
    def __init__(self, side):
        self.side = side 

    def area(self): 
        return self.side**2 
    
    def show(self): 
        print(f"Square Area = {self.area():.2f} m^2\n") 

#required function
def area(polygon):
    polygon.show()
    return polygon.area() 

#function to execute program
def main(): 
    triangle = Triangle(3, 2.6) 
    rectangle = Rectangle(2.12, 10) 
    square = Square(25) 

    print("\n----POLYGONE'S AREA----")
    area(rectangle)
    area(triangle) 
    area(square) 

if __name__ == "__main__": 
    main() 

