import streamlit as st

st.set_page_config(
    page_title="Smart Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Smart Calculator")
st.write("Calculator & Unit Converter")

menu = st.sidebar.selectbox(
    "Choose Module",
    ["Basic Calculator", "Unit Converter", "Currency Converter"]
)

if menu == "Basic Calculator":

    st.header("Basic Calculator")

    num1 = st.number_input("Enter First Number")
    num2 = st.number_input("Enter Second Number")

    operation = st.selectbox(
        "Select Operation",
        ["Addition", "Subtraction", "Multiplication", "Division"]
    )

    if st.button("Calculate"):

        if operation == "Addition":
            result = num1 + num2

        elif operation == "Subtraction":
            result = num1 - num2

        elif operation == "Multiplication":
            result = num1 * num2

        else:
            result = num1 / num2 if num2 != 0 else None

        if result is not None:
            st.success(f"Result: {result}")
        else:
            st.error("Cannot divide by zero!")

elif menu == "Unit Converter":

    st.header("Unit Converter")

    option = st.selectbox(
        "Choose Conversion",
        ["KM to Miles", "Celsius to Fahrenheit"]
    )

    value = st.number_input("Enter Value")

    if st.button("Convert"):

        if option == "KM to Miles":
            result = value * 0.621371

        else:
            result = (value * 9/5) + 32

        st.success(f"Converted Value: {result:.2f}")

elif menu == "Currency Converter":

    st.header("Currency Converter")

    option = st.selectbox(
        "Choose Conversion",
        ["INR to USD", "USD to INR"]
    )

    amount = st.number_input("Enter Amount", min_value=0.0)

    if st.button("Convert Currency"):

        if option == "INR to USD":
            result = amount / 85
            st.success(f"USD: ${result:.2f}")

        else:
            result = amount * 85
            st.success(f"INR: ₹{result:.2f}")