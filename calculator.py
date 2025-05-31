def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main():
    print("Welcome to the Simple Calculator!")
    print("Operations available: +, -, *, /")
    
    while True:
        num1 = get_number("Enter the first number: ")
        operation = input("Enter the operation (+, -, *, /): ")
        num2 = get_number("Enter the second number: ")
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operation! Please use one of +, -, *, /.")
            continue
        
        print(f"Result: {result}")
        
        # Ask if user wants to continue
        cont = input("Do you want to perform another calculation? (yes/no): ").lower()
        if cont != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
