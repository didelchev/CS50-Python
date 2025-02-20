import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_input()

    try:
        imageFile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')

    shirt_file = Image.open('shirt.png')

    size = shirt_file.size

    muppet = ImageOps.fit(imageFile, size)

    muppet.paste(shirt_file, shirt_file)

    muppet.save(sys.argv[2])





def check_input():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    first_file = splitext(sys.argv[1])
    second_file = splitext(sys.argv[2])

    if check_extension(first_file[1]) == False:
        sys.exit('Invalid output')

    if check_extension(second_file[1]) == False:
        sys.exit('Invalid output')

    if first_file[1].lower() != second_file[1].lower():
        sys.exit('Input and output have different extensions')



def check_extension(file):
    if file in ['.jpeg','.jpg','.png']:
        return True
    return False


if __name__ == '__main__':
    main()
