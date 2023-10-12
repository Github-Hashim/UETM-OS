"""
Software Construction and Development Lab no 2
Author: Muhammad Hashim
Dated: September 27, 2023
"""
def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers, handling division by zero"""
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    """Calculator function that takes user input and performs arithmetic operations"""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user input for the operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Get user input for the two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation and display the result
    if choice == "1":
        print("Result:", add(num1, num2))

    elif choice == "2":
        print("Result:", subtract(num1, num2))

    elif choice == "3":
        print("Result:", multiply(num1, num2))

    elif choice == "4":
        # Check for division by zero
        if num2 == 0:
            print("Result:", divide(num1, num2))
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid input")
