import streamlit as st

def main():
    st.title("WebApp Calculator")
    
    # User input fields
    num1 = st.number_input("Enter first number", value=0.0, step=0.1)
    num2 = st.number_input("Enter second number", value=0.0, step=0.1)
    
    # First row of operations
    col1, col2, col3, col4 = st.columns(4)
    result = None
    
    with col1:
        if st.button("➕ Addition"):
            result = num1 + num2
    with col2:
        if st.button("➖ Subtraction"):
            result = num1 - num2
    with col3:
        if st.button("✖️ Multiplication"):
            result = num1 * num2
    with col4:
        if st.button("➗ Division"):
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero")
    
    # Second row of operations
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        if st.button("Modulus (%)"):
            if num2 != 0:
                result = num1 % num2
            else:
                st.error("Cannot divide by zero")
    with col6:
        if st.button("Exponentiation (^)"):
            result = num1 ** num2
    with col7:
        if st.button("Floor Division (//)"):
            if num2 != 0:
                result = num1 // num2
            else:
                st.error("Cannot divide by zero")
    with col8:
        if st.button("Negation (-x)"):
            result = -num1
    
    # Display result
    if result is not None:
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
