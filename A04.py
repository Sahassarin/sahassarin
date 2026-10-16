class Calculator:
    def add(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

calc = Calculator()
print("Add:", calc.add(10, 5))
print("Subtraction:", calc.subtraction(10, 5))
print("Multiplication:", calc.multiplication(10, 5))
print("Divide:", calc.divide(10, 5))