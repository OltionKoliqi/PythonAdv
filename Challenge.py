def calculate(number1, number2, operator):
    try:
        # Check if the operator is addition
        if operator == '+':
            return number1 + number2

        # Check if the operator is subtraction
        elif operator == '-':
            return number1 - number2

        # Check if the operator is multiplication
        elif operator == '*':
            return number1 * number2

        # Check if the operator is division
        elif operator == '/':
            # Explicitly raise a ZeroDivisionError if the second number is zero
            if number2 == 0:
                raise ZeroDivisionError("Error: Division by zero is not allowed.")
            return number1 / number2

        # Raise a ValueError if the operator is invalid
        else:
            raise ValueError("Error: Invalid operator entered. Please use one of (+, -, *, /).")

    except ZeroDivisionError as e:
        # Handle division by zero error
        return str(e)

    except ValueError as e:
        # Handle invalid operator or input errors
        return str(e)

    except Exception as e:
        # Handle any other unexpected errors
        return f"Unexpected error: {e}"


# Prompt the user to enter the arithmetic operation and two numbers
try:
    # Prompt the user for the first number, second number, and operator
    number1 = float(input("Enter the first number: "))  # Convert input to float
    number2 = float(input("Enter the second number: "))  # Convert input to float

    # Prompt the user to enter the operator (+, -, *, /)
    operator = input("Enter the operator (+, -, *, /): ")

    # Call the calculate function with the user input
    result = calculate(number1, number2, operator)

    # Print the result of the calculation
    print(f"The result of {number1} {operator} {number2} is: {result}")

except ValueError as e:
    # Handle the case where the user inputs a non-numeric value
    print(f"Error: Invalid input. Please enter valid numbers. Details: {e}")

except Exception as e:
    # Catch any unexpected errors that occur during input or other operations
    print(f"Unexpected error: {e}")

finally:
    # This block will run no matter what, indicating the end of the program
    print("End of program. Thank you for using the calculator!")
