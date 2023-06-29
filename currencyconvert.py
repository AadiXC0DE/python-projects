def currency_converter(amount, from_currency, to_currency):
    exchange_rates = {
        "USD": {"EUR": 0.85, "GBP": 0.73, "JPY": 110.23},
        "EUR": {"USD": 1.18, "GBP": 0.86, "JPY": 128.87},
        "GBP": {"USD": 1.37, "EUR": 1.16, "JPY": 149.59},
        "JPY": {"USD": 0.0091, "EUR": 0.0078, "GBP": 0.0067}
    }

    if from_currency == to_currency:
        return amount

    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        return "Conversion not available for the given currencies."


amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency to convert from (e.g., USD, EUR, GBP, JPY): ")
to_currency = input("Enter the currency to convert to (e.g., USD, EUR, GBP, JPY): ")

converted_amount = currency_converter(amount, from_currency, to_currency)
if type(converted_amount) == str:
    print(converted_amount)
else:
    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
