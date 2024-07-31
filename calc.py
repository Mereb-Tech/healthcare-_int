import sys

def calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operation!"

def main():
    while True:
        # Get user input
        user_input = input("Enter command (or type 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Exiting...")
            break

        # Split the input into components
        parts = user_input.split()

        if len(parts) != 3:
            print("Usage: <num1> <num2> <operation>")
            print("Operation: add, subtract, multiply, divide")
            continue

        try:
            num1 = float(parts[0])
            num2 = float(parts[1])
            operation = parts[2].lower()
        except ValueError:
            print("Error: Both num1 and num2 must be valid numbers.")
            continue

        result = calculator(num1, num2, operation)
        print("Result:", result)

# if __name__ == "__main__":
    # main()
