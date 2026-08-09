#คำนวณสี่เหลี่ยมผืนผ้า
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

#คำนวณสามเหลี่ยม
def calculate_triangle_area(height, base):
    """Calculates and displays triangle area"""
    area = 0.5 * height * base
    print(f"triangle with height {height} and base {base}")
    print(f"Area = {height} × {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)

# จากตัวอย่าง ให้สร้าง functionn สำหรับคำนวณเพท.วงกลม
def calculate_circle_area(radius):
    """Calculates and displays circle area"""
    area =  3.14159 * radius**2
    print(f"circle with and radius {radius}")
    print(f"Area = 3.14 x {radius} = {area}")
    print()

print("Calculating circle areas:")
calculate_circle_area(5)
calculate_circle_area(10)

# จากตัวอย่างด้านบน ให้เขียน function ชื่อ square_root(n):
def square_root(n):
    return n ** 0.5

print("Using return values in expressions:")
result = multiply(4, 5) + square(3)
print(f"multiply(4, 5) + square(3) = {multiply(4, 5)} + {square(3)} = {result}")
print()

print(f"square root of 25 =", square_root(25))
print()