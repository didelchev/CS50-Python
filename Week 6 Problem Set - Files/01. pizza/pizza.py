# [] command line arg
# []
# print(tabulate(table, headers, tablefmt="grid"))

import sys
import csv
from tabulate import tabulate

def main():
    file_name = get_file_name()
    read_file(file_name)



def get_file_name():
    user_input = sys.argv[1:]
    if len(user_input) < 1:
        sys.exit('Too few command-line arguments')
    elif len(user_input) > 1 :
        sys.exit('Too many command-line arguments')
    file_name = ''.join(user_input)
    if not file_name.endswith('.csv'):
        sys.exit('Not a CSV file')
    else:
        return file_name


def read_file(input):
    with open(input, 'r') as file:
       list_pizza = []
       lines = csv.DictReader(file)
       for line in lines:
           list_pizza.append(line)
    print(tabulate(list_pizza,headers = 'keys',tablefmt='grid'))




if __name__ == "__main__":
    main()
pro