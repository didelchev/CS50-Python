# [x] install inflect
# [x] create a funct
# [x] start prompting the user for input
# [x] store the names in a list
# [] separate the names properly
# [] bind adieu to the name
# [] print the names with adieu binded to them


import inflect
p = inflect.engine()
def adieu():
    list = []
    try:
        while True:
            user_input = input('Name: ')
            goodbye = 'Adieu, adieu, to '
            list.append(user_input)
            newList = p.join(list)
    except EOFError:
        print('\n'+goodbye + newList)
        pass



adieu()
