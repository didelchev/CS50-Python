felipe_shop = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def get_user_input():
    total = 0
    while True:
        try:
            user_input = input('Item: ').lower().title()
            if user_input in felipe_shop:
                total += felipe_shop[user_input]
                formated_total = "%.2f" % total
                print(f'Total: ${formated_total}')
        except EOFError:
                print("\n")
                break
get_user_input()
