import sys
import requests
import json

#Add your apikey by logging in coin cap website.
api_key = 'Your_API_KEY here.'
def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument.")
    elif len(sys.argv) == 2:
        try:
            number_of_bitcoin = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number.")
    else:
        sys.exit()
    response = requests.get(f'https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}')
    data = response.json()
    price = float(data["data"]["priceUsd"])
    amount = number_of_bitcoin * price
    print(f"${amount:,.4f}")
    
main()