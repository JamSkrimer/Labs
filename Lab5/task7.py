import math

def point_in_circle(x, y, radius):
    return math.sqrt(x**2 + y**2) <= radius

x = float(input("Координата x: "))
y = float(input("Координата y: "))
radius = float(input("Радиус: "))

if point_in_circle(x, y, radius):
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")