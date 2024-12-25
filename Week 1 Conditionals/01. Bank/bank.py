def check_greeting():
#Accept user input and format
    answer = input('Greeting: ').lower().strip()
#Check if answer includes the word 'hello', print 0
    if 'hello' in answer:
        print('$0')
#Check if the answer starts with thw letter 'h', print $20
    elif answer.startswith('h') and answer != 'hello':
        print('$20')
#Otherwise, print $100
    else :
        print('$100')




check_greeting()



