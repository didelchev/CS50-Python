def main():
    user_input = input("camelCase: ")
    convert_to_snake_case(user_input)

def convert_to_snake_case(words):
    print('snake_case: ', end="")
    for  letter in words:
        if(letter.isupper()):
           print("_" + letter.lower(), end="")
        else:
            print(letter, end = "")
    print()
main()
