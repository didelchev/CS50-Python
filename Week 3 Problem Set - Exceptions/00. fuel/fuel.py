# create a dictionaty with the fuel tank
import math

fuel_tank = {'0/1': 'E',
             '1/4': '25%',
             '1/2': '50%',
             '3/4': '75%',
             '4/4': 'F'
             }
# Get the user input
def get_user_input():
    while True:
        try:
            user_input = input('Fraction: ').split("/")
            x = int(user_input[0])
            y = int(user_input[1])
            percentage = (x/y)*100

            if x > y:
                user_input
            else:
                return int(percentage)

        except ValueError:
            user_input
            print("Invalid input format !!!")
        except ZeroDivisionError:
            user_input
            print("Cannot divide by zero !!!")
        except:
            user_input
            print("Invalid input !")




def calc_fuel(input):
    if input <= int(1):
        print("E")
    elif input == int(25):
        print("25%")
    elif input == int(50):
        print("50%")
    elif input == int(75):
        print("75%")
    elif math.floor(input) == int(33):
        print("33%")
    elif math.ceil(input)  == int(67):
        print("67%")
    elif input >= int(99):
        print("F")






calc_fuel(get_user_input())


# check the user input

# print result

# if fuel_tank.get(user_input):
#         print(fuel_tank.get(user_input))
# except (ValueError, ZeroDivisionError):
#         print('Invalid input')
