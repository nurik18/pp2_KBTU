import math

#1
def degreesToRadians(degrees):
    return degrees * (math.pi / 180)

degrees = 15
radians = degreesToRadians(degrees)
print(f"{degrees} градусов = {radians} радиан")

#2
def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

base1 = 5
base2 = 6
height = 5
area = trapezoid_area(base1, base2, height)
print(f"Площадь трапеции: {area}")

#3
def regular_polygon_area(sides, length):
    return (sides * length ** 2) / (4 * math.tan(math.pi / sides))

sides = 4
length = 25  
area = regular_polygon_area(sides, length)
print(f"Площадь правильного многоугольника: {area}")

#4
def parallelogram_area(base, height):
    return base * height

base = 5 
height = 6
area = parallelogram_area(base, height)
print(f"Площадь параллелограмма: {area}")
