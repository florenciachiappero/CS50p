# In a file called bitcoin.py, implement a program that:

# Expects the user to specify as a command-line argument the number of 
# Bitcoins, , that they would like to buy. If that argument cannot be 
# converted to a float, the program should exit via sys.exit with an 
# error message.
# Queries the API for the CoinDesk Bitcoin Price Index at 
# https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON 
# object, among whose nested keys is the current price of Bitcoin as a 
# float. Be sure to catch any exceptions.


import sys
import requests


def main():
    value = check_argv()

    # Get current price of Bitcoin and the total amount
    total_amount = (price_bitcoin(value))

    # Print total amount
    print(f"${total_amount:,.4f}")


def check_argv():
    # Get value from command-line
    if len(sys.argv) == 2:
        try:
            return float(sys.argv[1])
        except:
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)


def price_bitcoin(value):
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprince.json')
        response = r.json()
        bitcoin = response['bpi']['USD']['rate_float']
        return bitcoin * value

    except requests.RequestException:
        print("RequestException")
        sys.exit(1)


if __name__ == "__main__":
    main()
