import streamlit as st

def main():
    st.title("WebApp Calculator")
    
    # User input fields
    num1 = st.number_input("Enter first number", value=0.0, step=0.1)
    num2 = st.number_input("Enter second number", value=0.0, step=0.1)
    operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])
    
    # Perform calculation
    result = None
    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero")
    
    # Display result
    if result is not None:
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
