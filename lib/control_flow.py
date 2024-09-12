# control_flow.py

def admin_login(username, password):
    """returns 'Access granted' for username=admin and password=12345, otherwise 'Access denied'."""
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    return "Access denied"

def hows_the_weather(temperature):
    """returns a string based on the temperature."""
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature <= 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"

def fizzbuzz(num):
    """returns 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, 'FizzBuzz' for multiples of both, or the number itself otherwise."""
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return num

def calculator(operation, a, b):
    """returns the result of the operation between a and b, or prints 'Invalid operation!' if the operation is not recognized."""
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        print("Invalid operation!")
        return None
