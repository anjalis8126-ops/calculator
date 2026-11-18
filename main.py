print("===== INTERACTIVE CALCULATOR =====")


# INPUT VALIDATION FUNCTION

def get_number(message):

    while True:
        try:
            number = float(input(message))
            return number

        except ValueError:
            print("Invalid input! Enter a number.")


# BASIC CALCULATOR

def basic_calculator():

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose operation: ")

    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":

        if num2 != 0:
            print("Result:", num1 / num2)

        else:
            print("Cannot divide by zero!")

    else:
        print("Invalid choice!")


# UNIT CONVERTER

def unit_converter():

    while True:

        print("\n===== UNIT CONVERTER =====")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Back to Main Menu")

        choice = input("Choose conversion: ")

        if choice == "1":

            km = get_number("Enter distance in KM: ")
            miles = km * 0.621371

            print("Miles:", miles)

        elif choice == "2":

            celsius = get_number("Enter temperature in Celsius: ")
            fahrenheit = (celsius * 9/5) + 32

            print("Fahrenheit:", fahrenheit)

        elif choice == "3":
            break

        else:
            print("Invalid choice!")

            # CURRENCY CONVERTER

def currency_converter():

    while True:

        print("\n===== CURRENCY CONVERTER =====")
        print("1. INR to USD")
        print("2. USD to INR")
        print("3. Back to Main Menu")

        choice = input("Choose conversion: ")

        # Example fixed exchange rate
        rate = 85

        if choice == "1":

            inr = get_number("Enter amount in INR: ")

            usd = inr / rate

            print("Amount in USD:", round(usd, 2))

        elif choice == "2":

            usd = get_number("Enter amount in USD: ")

            inr = usd * rate

            print("Amount in INR:", round(inr, 2))

        elif choice == "3":
            break

        else:
            print("Invalid choice!")


# MAIN MENU

while True:

    print("\n===== MAIN MENU =====")
    print("1. Basic Calculator")
    print("2. Unit Converter")
    print("3. Currency Converter")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        basic_calculator()

    elif choice == "2":
        unit_converter()

    elif choice == "3":
        currency_converter()

    elif choice == "4":
        print("Thank you for using our program!")
        break

    else:
        print("Invalid choice! Try again.")