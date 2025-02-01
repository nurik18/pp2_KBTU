# 2
class Shape:
    def area(self):
        print(0)


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length ** 2)

# 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

shape = Shape()
square = Square(5)
rect = Rectangle(3, 4)

shape.area()
square.area()
rect.area() 
