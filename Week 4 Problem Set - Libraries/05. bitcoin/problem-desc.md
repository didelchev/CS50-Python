### Problem description

In a file called bitcoin.py, implement a program that:

    Expects the user to specify as a command-line argument the number of Bitcoins,

, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

import requests

try:
...
except requests.RequestException:
...

Outputs the current cost of
Bitcoins in USD to four decimal places, using , as a thousands separator.
