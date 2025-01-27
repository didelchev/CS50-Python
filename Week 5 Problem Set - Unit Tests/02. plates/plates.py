# def main():
#     plate = input("Plate: ").upper()
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")



# def is_valid(s):
#     for letter in s:

# #Plate must start with 2 letters
#         if len(s) < 2 or len(s) > 6:
#             return False
# #Plate max characters 6 and minimum 2 chars
#         elif not s[0].isalpha() or not s[1].isalpha():
#             return False
# # No periods, space or punctuation etc..
#         elif not s.isalnum():
#             return False
#         else:
#             return True

# main()


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    for c in s:
        if c in ['.',' ', '!', '?']:
            return False
    return True

if __name__ == "__main__":
    main()
