import random


def main():
    level = get_level()

    score = generate_game(level)

    print("Score: ", score)



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1,4):
                break;
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x,y

def generate_round(x,y):
    user_tries = 1
    while user_tries < 3:
        try:
            answer = int(input(f'{x} + {y} = '))
            if answer == (x + y):
                return True
            else:
                user_tries += 1
                print('EEE')
        except:
            user_tries += 1;
            print("EEE")
    print(f'{x} + {y} = {x + y}')
    return False


def generate_game(level):
    rounds = 1
    score = 0

    while rounds <= 10:
        x, y = generate_integer(level);
        user_answer = generate_round(x,y)
        if user_answer == True:
            score += 1
        rounds += 1
    return score





if __name__ == "__main__":
    main()
