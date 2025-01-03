def find_answer():
    answer = input(
        'What is the Answer to the Great Question of Life, the Universe, and Everything?')

    match answer.lower().strip():
        case '42':
            print('Yes')
        case 'forty-two':
            print('Yes')
        case 'forty two':
            print('Yes')
        case _:
            print('No')


find_answer()
