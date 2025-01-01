# Create a function
def vowel_remover():
    # Create volwes list
    vowels = ['a', 'e', 'i', 'o', 'u']
# Get user input
    user_input = input('Input: ')
    print("Output: ", end="")

# Check the input for volwes
    for letter in user_input:
        if not letter.lower() in vowels:
            print(letter, end="")
    print()

vowel_remover()
