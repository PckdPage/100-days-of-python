name = input("Enter your name: ")
print(f"Hello, {name}")

num1 = int(input("Enter a number: "))
num1 = str(num1)
print(f"Number doubled: {num1 * 2}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2

print(f"The sum of {num1} and {num2} is {result}")

a = 5
b = 3

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")

# Simple Calculator

# Step 1: Get user input for two numbers
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

# Step 2: Perform arithmetic operation
add = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2 if num2 != 0 else "Cannot divide by zero"

# Step 3: Display the results
print("\n--- Calculator Results ----")
print(f"Addition:{n1} + {n2} = {add}")
print(f"Subtraction:{n1} - {n2} =  {sub}")
print(f"Multiplication:{n1} x {n2} =  {mult}")
print(f"Division:{n1} / {n2} =  {div}")