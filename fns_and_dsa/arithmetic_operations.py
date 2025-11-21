#!/usr/bin/env python3

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations: add, subtract, multiply, divide.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform: 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float or str: Result of the operation, or an error message if division by zero occurs or operation is invalid.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation. Choose add, subtract, multiply, or divide."

