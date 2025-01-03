def check_file():
    user_input = input('File name: ').lower().strip()
    if '.jpg' in user_input:
        print('image/jpeg')
    elif '.jpeg' in user_input:
        print('image/jpeg')
    elif '.png' in user_input:
        print('image/png')
    elif '.gif' in user_input:
        print('image/gif')
    elif '.pdf' in user_input:
        print('application/pdf')
    elif '.zip' in user_input:
        print('application/zip')
    elif '.txt' in user_input:
        print('text/plain')
    else:
        print('application/octet-stream')

check_file()
