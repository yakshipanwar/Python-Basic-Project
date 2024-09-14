"""
Calculator Program

This program allows users to perform basic arithmetic operations (+, -, *, /) on two numbers.

Example:
    Enter first number: 5
    Enter Second number: 2
    Enter the operator: +
    Output: a + b = 7

Parameters:
    a (int): The first number
    b (int): The second number
    operator (str): The operator (+, -, *, /)

Returns:
    None

"""
while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter Second number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    if operator == '+':
        print("a + b =", (a+b))
    elif operator == '-':
        print("a - b =", (a-b))
    elif operator == '*':
        print("a * b =", (a*b))
    elif operator == '/':
        if b != 0:
            print("a / b =", (a/b))
        else:
            print("Error: Division by zero is not allowed")
    else:
        break