from emoji import emojize

def return_emoji():
    user_input = input('Input: ')

    print("Output: " + emojize(user_input, language='alias'))


return_emoji()
