# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b

def main():
    print("Simple Command-Line Calculator")
    print("Operations: +, -, *, /")
    print("Type 'exit' to quit.\n")

    while True:
        operation = input("Enter any  operation (+, -, *, /) or 'exit': ").strip()
        
        if operation.lower() == 'exit':
            print("Exiting calculator.")
            break
        
        if operation not in ('+', '-', '*', '/'):
            print("Invalid operator. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter only  numeric values.")
            continue

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        print(f"Result: {result}\n")
        
if __name__ == "__main__":
   main()