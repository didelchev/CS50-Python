# [x] get csv file
# [x] get correct input
# [x] read the file
# [x] split the rows
# [x] get first_name, last_name and house
# [x] write them in a new file with 3 columns

import sys
import csv


def main():
    get_file_names()

    output = []

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_name, first_name = row['name'].split(',')
                house = row['house']
                output.append(
                    {'first': first_name.lstrip(), 'last': last_name, 'house': house})

    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(
            file, fieldnames=['first', 'last', 'house'])
        writer.writerow(
            {'first': 'first', 'last': 'last', 'house': 'house'})

        for row in output:
            writer.writerow(
                {'first': row['first'], 'last': row['last'], 'house': row['house']})


def get_file_names():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if '.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]:
        sys.exit('Not a CSV file')


if __name__ == "__main__":
    main()
