while True :
    first_fhandle = input('Enter a file name: ')
    try:
        open_first_file = open(first_fhandle)
        break
    except:
        print('File', first_fhandle, 'cannot be opened. Try again.')

while True :
    second_fhandle = input('Enter another file name: ')
    try:
        open_second_file = open(second_fhandle)
        break
    except:
        print('File', second_fhandle, 'cannot be opened. Try again.')

print(open_first_file)
print(open_second_file)