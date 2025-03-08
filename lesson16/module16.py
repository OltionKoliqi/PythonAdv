import streamlit as st

def calculate(num1, num2, operator):
    if operator == 'Addition':
        return num1 + num2
    elif operator == 'Subtract':
        return num1 - num2
    elif operator == 'Multiply':
        return num1 * num2
    elif operator == 'Divide':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by 0'

st.title("Simple Calculator")


def main():
    num1 = st.number_input("Enter the first number", value=0)
    num2 = st.number_input("Enter the second number", value=0)
    operation = st.radio("Chose an operation",["Addition", "Subtract", "Multiply", "Divide"])

    result = calculate(num1, num2, operation)

    st.write(f"Result of the {operation} of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()