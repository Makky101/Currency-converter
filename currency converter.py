#currency converter
import requests


API_KEY = 'fca_live_pGvfjA7m9OggBoa91089ssrNSsGNTh6geijmF8Lu'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ["USD", "EUR", "GBP", "CAD", "AUD", "JPY", "CNY", "INR", "CHF", "NZD"]



def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print("Invalid currency.")
        return None
    
while True:
    base = input("Enter the base currency (q for quit): ").upper()
    if base == "Q":
        break

    num = int(input("Enter Amount: "))

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value * num}")