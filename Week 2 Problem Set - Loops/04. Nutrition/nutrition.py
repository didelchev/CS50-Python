def calorie_counter():
    user_input = input("Item: ")
    # print("Calories: ", end="")
    products = [
        {"item": "Banana", "calories": "110"},
        {"item":"Apple", "calories":"130"},
        {"item": "Avocado", "calories": "50"},
        {"item": "Kiwifruit", "calories": "90"},
        {"item": "Pear", "calories": "100"},
        {"item": "Sweet Cherries", "calories":"100"}
    ]

    for product in products:
        if user_input.lower() == product["item"].lower():
            print("Calories: " + product["calories"])
calorie_counter()

