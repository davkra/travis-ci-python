def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b
