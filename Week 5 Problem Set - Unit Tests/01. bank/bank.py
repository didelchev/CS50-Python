# def check_greeting():
# #Accept user input and format
#     answer = input('Greeting: ').lower().strip()
# #Check if answer includes the word 'hello', print 0
#     if 'hello' in answer:
#         print('$0')
# #Check if the answer starts with thw letter 'h', print $20
#     elif answer.startswith('h') and answer != 'hello':
#         print('$20')
# #Otherwise, print $100
#     else :
#         print('$100')

# check_greeting()



def main():
    user_input = input('Greeting: ')

    money_to_print = value(user_input)

    print(f'${money_to_print}')


def value(greeting):
    greeting = greeting.lower().strip()
    if 'hello' in greeting:
       return 0
#Check if the answer starts with thw letter 'h', print $20
    elif greeting.startswith('h') and greeting != 'hello':
        return 20
#Otherwise, print $100
    else :
        return 100


if __name__ == "__main__":
    main()

