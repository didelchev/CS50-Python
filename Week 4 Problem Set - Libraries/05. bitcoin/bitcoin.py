# Get the user command line argument
# Convert the argument to float
    # If it cant be conveted the program should exit => sys.exit
# Get Bitcoin price
#


import requests
import sys
import json


def get_user_input():
    if len(sys.argv) == 2:
        return(sys.argv[1])
    elif len(sys.argv) < 2:
        sys.exit('Missing command-line argument')
    else:
        sys.exit




def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    api_request = requests.get(url).json()

    bitcoin_price = api_request['bpi']['USD']['rate_float']

    return bitcoin_price


def calculate_bitcoin():
    bitcoin_price = get_bitcoin_price()
    user_input = float(get_user_input())

    result = bitcoin_price * user_input

    print(f"${result:,.4f}")





calculate_bitcoin()
s