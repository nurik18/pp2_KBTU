import math

# 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates of the point: ({self.x}; {self.y})")

    def moveNSave(self, xx, yy):   # меняет переменную и сохраняет
        print(f"({self.x}; {self.y})")
        self.x += xx
        self.y += yy
        print(f"({self.x}; {self.y})")
# ВАЖНО !! Использовать либо одну либо другую, выводят одинаково
    def moveNShow(self, xx, yy):    # переменную не трогает
        print(f"({self.x}; {self.y})")
        print(f"({self.x+xx}; {self.y+yy})")
    
    def dist(self, otherPoint):
        print(math.sqrt((self.x-otherPoint.x)**2 + (self.y-otherPoint.y)**2))

point1 = Point(2,3)
point2 = Point(1,2)

point1.show()

# Следующий кусок кода важен т.к. после него идет работа с переменными(метод dist)
temp = int(input("1 - Если хотите сохранить изменение в переменную\n2 - Если не хотите работать с переменной\nВаше число: "))
if temp == 1:  
    point1.moveNSave(1,1)

else:
    point1.moveNShow(1,1)

point1.dist(point2)