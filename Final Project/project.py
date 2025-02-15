# [x] Get User Input - age, weight, height, activity ?
# [x] Calculate TDEE
# [] Option to loose weight
# [] Option to gain weight 
# [] Option to maintain weight


def main():
    user_data = get_user_input()
    calculate_calories(user_data)


def get_user_input():
    activity = {
        "Sedentary (little to no exercise)": float(1.2),
        "Light exercise (1-3 days per week)": float(1.375),
        "Moderate exercise (3-5 days per week)" : float(1.55),
        "Heavy exercise (6-7 days per week)" : float(1.725),
        "Very heavy exercise (Twice per day,intense)" :float(1.9)
    }
    
    try:
        age = int(input('Age: '))
        weight = int(input('Weight: '))
        height = int(input('Height: '))
 
        print("What is your activity level ?")
    
        for index, key in enumerate(activity.keys(), start=1):
            print(f'  {index}) {key}')

        user_activity = int(input("Please select the number of the activity level: "))

        if user_activity == 1:
            return{
                'age': age,
                'weight': weight,
                'height': height,
                'activity': activity['Sedentary (little to no exercise)']
            }
        elif user_activity == 2:
            return{
                'age': age,
                'weight': weight,
                'height': height,
                'activity': activity['Light exercise (1-3 days per week)']
            }
        elif user_activity == 3:
            return{
                'age': age,
                'weight': weight,
                'height': height,
                'activity': activity['Moderate exercise (3-5 days per week)']
            }
        elif user_activity == 4:
            return{
                'age': age,
                'weight': weight,
                'height': height,
                'activity': activity['Heavy exercise (6-7 days per week)']
            }
        elif user_activity == 5:
            return{
                'age': age,
                'weight': weight,
                'height': height,
                'activity': activity['Very heavy exercise (Twice per day,intense)']
            }
    except ValueError:
        print('Invalid input !')


def calculate_calories(input):
    age, weight, height, activity = input.values()

    base_metabolic_rate = ( 10 * weight) + ( 6.25 * height) - ( 5 * age) + 5

    total_calories = base_metabolic_rate * activity

    print(f'Your daily calories to maintain weight are: {int(total_calories)} kcals')

    input()
    

       
    
    


if __name__ == '__main__':
    main()