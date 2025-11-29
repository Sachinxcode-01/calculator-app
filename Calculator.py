def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("Welcome to Simple Calculator")
    while True:
        print("\nOptions: add, subtract, multiply, divide, exit")
        choice = input("Enter operation: ").lower()
        if choice == "exit":
            print("Exiting calculator. Goodbye!")
            break
        if choice in ("add", "subtract", "multiply", "divide"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers.")
                continue

            if choice == "add":
                print("Result:", add(num1, num2))
            elif choice == "subtract":
                print("Result:", subtract(num1, num2))
            elif choice == "multiply":
                print("Result:", multiply(num1, num2))
            elif choice == "divide":
                print("Result:", divide(num1, num2))
        else:
            print("Invalid operation! Try again.")

if __name__ == "__main__":
    calculator()
