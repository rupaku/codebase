try:
    with open('file1.txt','r') as file:
        print(file.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err