import streamlit as st
import math

def evaluate_expression(expression):
    try:
        # Replace special symbols with Python-compatible functions
        expression = expression.replace("x²", "**2").replace("x³", "**3")
        expression = expression.replace("√x", "math.sqrt").replace("ln", "math.log")
        expression = expression.replace("log₁₀", "math.log10").replace("π", "math.pi")
        expression = expression.replace("cos", "math.cos").replace("sin", "math.sin").replace("tan", "math.tan")
        expression = expression.replace("e^x", "math.exp")
        
        # Evaluate the mathematical expression
        result = eval(expression, {"math": math, "__builtins__": None}, {})
        return str(result)
    except Exception:
        return "Error"

def main():
    st.title("Scientific Calculator")
    
    # Display for selected numbers and operation
    result_display = st.empty()
    
    # Store user selections in session state
    if 'expression' not in st.session_state:
        st.session_state.expression = ""
    
    # Number and operation buttons
    buttons = [
        ["(", ")", "mc", "m+", "m-", "mr"],
        ["C", "x²", "x³", "e^x", "10^x", "/"],
        ["7", "8", "9", "√x", "ln", "*"],
        ["4", "5", "6", "log₁₀", "-", "+"] ,
        ["1", "2", "3", "EE", "Rad", "="] ,
        ["0", ".", "π", "cos", "sin", "tan"]
    ]
    
    for row in buttons:
        cols = st.columns(len(row))
        for idx, btn in enumerate(row):
            with cols[idx]:
                if st.button(btn):
                    if btn == "C":
                        st.session_state.expression = ""
                    elif btn == "=":
                        st.session_state.expression = evaluate_expression(st.session_state.expression)
                    else:
                        st.session_state.expression += btn
    
    # Display current expression
    result_display.text_input("Expression", st.session_state.expression, disabled=True)
    
if __name__ == "__main__":
    main()