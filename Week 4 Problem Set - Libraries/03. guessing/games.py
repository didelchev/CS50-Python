# 1.[x] import random
# 2.[x] create a function
# 3.[x] Prompt the user for input (level)
    # [x] If its not int -> prompt again
    # [x] Randomly generate a number between 1 and 'n'
# [x] Prompt the user again to guess the number
    # If its not positive -> prompt again
# [x] Check the guess
    # [x] If the guess < num -> print('Too small!') and prompt again
    # [x] If the guess > num -> print('Too large!') and prompt again
    # [x] If the guess = num -> print('Just right!') and exit

import random

def guess_the_num():

    while True:
        try:
            user_level = int(input('Level: '));
            if user_level > 0:
                break
        except:
            pass

    while True:
        try:
            random_num = random.randint(1, user_level)
            user_guess = int(input('Guess: '))
            if user_guess < random_num:
                print('Too small!')
            elif user_guess > random_num:
                print('Too large!')
            else:
                print('Just right!')
                break
        except:
            pass

guess_the_num()
