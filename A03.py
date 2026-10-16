import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return math.pi * self.radius ** 2

    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.radius

r = float(input("Enter the radius: "))
c = Circle(r)
print("Area:", c.calculate_circle_area())
print("Perimeter:", c.calculate_circle_perimeter())