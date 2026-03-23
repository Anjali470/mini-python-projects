def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = "You cannot divide by zero!!"
        return result

def power(base, exponent):
    return base ** exponent

def modulus(a, b):
    return a % b

oprations = {1: ("Addition", add),
             2: ("Subtraction", subtract),
             3: ("Multiplication", multiply),
             4: ("Division", divide),
             5: ("Power", power),
             6:("Modulus", modulus)}

def main():
    while True:
        print("1. Add\n"
              "2. Subtract\n"
              "3. Multiply\n"
              "4. Divide\n"
              "5. Power\n"
              "6. Modulus\n"
              "7. Exit")

        try:
            choice = float(input("Enter your choice: "))
        except ValueError:
            print("Enter a valid number")
            continue

        if choice not in range(1, 8):
            print("Please enter a valid choice")
            continue
        elif choice == 7:
            print("Exiting from the program!!")
            break

        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Enter a valid number")
            continue

        operation_name, operation_function = oprations[choice]

        result = operation_function(num1, num2)

        if type(result) == str:
            print(result)
        else:
            print(f"{operation_name} of {num1} and {num2} is {result}")

if __name__ == '__main__':
    main()