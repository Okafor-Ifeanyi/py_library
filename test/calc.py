def add(x, y):
    # Add Function
    return x + y

def subtract(x, y):
    # Add Function
    return x - y

def multiply(x, y):
    # Multiply Function
    return x * y

def divide(x, y):
    # Divide Function
    if y == 0:
        raise ValueError("Can't divide by 0")
    return x / y