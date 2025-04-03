import streamlit as st

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
                        try:
                            result = eval(st.session_state.expression)
                            st.session_state.expression = str(result)
                        except:
                            st.session_state.expression = "Error"
                    else:
                        st.session_state.expression += btn
    
    # Display current expression
    result_display.text_input("Expression", st.session_state.expression, disabled=True)
    
if __name__ == "__main__":
    main()