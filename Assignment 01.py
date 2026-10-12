class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

v = Vehicle(100, 10)
print(v.max_speed)
print(v.mileage)

import math

class Circle:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

c = Circle()
print("Area:", c.calculate_circle_area(5))