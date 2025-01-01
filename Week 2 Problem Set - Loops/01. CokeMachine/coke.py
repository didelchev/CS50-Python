# Create the function
def calc_change():
    # Get user input
    coins_amount = 50
    print(f"Amount Due: {coins_amount}")
    user_amount = 0

    while True:
        user_input = int(input('Insert Coin: '))
        user_amount += user_input
        print(f"Amount Due: {coins_amount - user_amount}")
        # Check the coin type
        while user_input != 25 and user_input != 10 and user_input != 5:
            print(f"Amount Due: {coins_amount}")
            user_input = int(input('Insert Coin: '))

        # Check if the coins has reached the target amount
        if user_amount >= coins_amount:
            change = abs(coins_amount - user_amount)
            # Print the change owed
            print(f"Change Owed: {change}")
            break

calc_change()
