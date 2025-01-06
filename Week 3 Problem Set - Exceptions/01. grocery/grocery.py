# get user input case insensitive

# Create dictionary

# Create a try / catch block

# Store the user input in

# Print the input in uppercase, sorted aplhab.

# End the input on EOFERROR


def grocery_list():
    list = {}
    while True:
        try:
            user_input = input().lower()
            if user_input not in list:
                list[user_input] = 1
            else:
                list[user_input] += 1
        except EOFError:
                sorted_items = sorted(list.items())
                for item, count in sorted_items:
                     print(f'{count} {item.upper()}')
                break
grocery_list()
