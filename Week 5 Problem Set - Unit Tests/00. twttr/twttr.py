# # Create a function
# def vowel_remover():
#     # Create volwes list
#     vowels = ['a', 'e', 'i', 'o', 'u']
# # Get user input
#     user_input = input('Input: ')
#     print("Output: ", end="")

# # Check the input for volwes
#     for letter in user_input:
#         if not letter.lower() in vowels:
#             print(letter, end="")
#     print()

# vowel_remover()

vowels = ['a', 'e', 'i', 'o', 'u']
def main():
    user_input = input('Input: ')
    word_without_vowels = shorten(user_input)
    print("Output: " + word_without_vowels)



def shorten(word):
    without_vowels = ''
    for letter in word:
        if not letter.lower() in vowels:
            without_vowels += letter
    return without_vowels



if __name__ == "__main__":
    main()
