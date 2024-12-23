# Create function convert
def convert(message):

    return message.replace(':)', '🙂').replace(':(','🙁 ')


def main():

    userInput = input();

    convert(userInput)

    print(convert(userInput))

main()
