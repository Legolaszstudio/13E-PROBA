def divide(a, b):
    return a / b

if __name__ == "__main__":
    print(divide(10, 2))
    print(divide(5, 2))
    try:
        print(divide(5, 0))
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
