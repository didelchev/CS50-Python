# [x]  prompt the user for command line input
# [x]  read the file and count the lines
# [x]  ignore whitespace and # signs
# [x]  If the user does not specify exactly one command-line argument,
# [x]  If the specified file’s name does not end in .py,
# [x]  If the specified file does not exist, the program should instead exit via sys.exit.


import sys

def main():
    file_name = get_file_name()
    file_line = read_file(file_name)
    print(file_line)


def get_file_name():
    user_input = sys.argv[1:]
    if len(user_input) < 1:
        sys.exit('Too few command-line arguments')
    elif len(user_input) > 1 :
        sys.exit('Too many command-line arguments')
    file_name = ''.join(user_input)
    if not file_name.endswith('.py'):
        sys.exit('Not a Python file')
    else:
        return file_name


def read_file(input):
    try:
        with open(input, 'r') as file:
            lines = file.readlines()
            line_count = 0
            for line in lines:
               if not (line.isspace() or line.lstrip().startswith("#")):
                   line_count += 1
            return line_count

    except FileNotFoundError:
        sys.exit('File does not exist')

if __name__ == "__main__":
    main()

