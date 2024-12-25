def calculate():
    user_input = input("Expression: ")
    x, y, z = user_input.split(" ")
    result = 0

    new_x = float(x)
    new_z = float(z)

    match y:
        case "+":
         result = new_x + new_z;
        case "-":
            result = new_x - new_z
        case "*":
            result = new_x * new_z
        case "/":
            result = new_x / new_z
        case _:
            print('Invalid operator')

    print(result)


calculate()
