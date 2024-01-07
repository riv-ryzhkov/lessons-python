#  pip install forex-python

from forex_python.converter import CurrencyRates


def currency_converter():
    c = CurrencyRates()

    print("Welcome to the Currency Converter!")
    print("Available currencies:")
    print(", ".join(c.get_rates("").keys()))

    # Get user input for conversion
    from_currency = input("Enter the source currency: ").upper()
    to_currency = input("Enter the target currency: ").upper()

    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Perform the currency conversion
    try:
        rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * rate

        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    currency_converter()