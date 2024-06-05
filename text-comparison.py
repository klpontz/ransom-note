# Prompt user for the first file name and handle errors
while True :
    first_fhandle = input('Enter a file name: ')
    if len(first_fhandle) < 1 : first_fhandle = "ransom.txt"
    try:
        open_first_file = open(first_fhandle)
        break
    except:
        print('File', first_fhandle, 'cannot be opened. Try again.')

# Prompt user for the second file name and handle errors
while True :
    second_fhandle = input('Enter another file name: ')
    if len(second_fhandle) < 1 : second_fhandle = "magazine.txt"
    try:
        open_second_file = open(second_fhandle)
        break
    except:
        print('File', second_fhandle, 'cannot be opened. Try again.')

# Initialize dictionaries to store character counts
first_hash = dict ()
second_hash = dict ()

# Read through the first file and count characters
for lines in open_first_file :
    lines = lines.strip()
    if len(lines) < 1 : 
        continue
    for letter in lines :
        if letter.isalpha() :
            letter = letter.lower()    
            first_hash[letter] = first_hash.get(letter, 0) + 1

# Read through the first file and count characters
for lines in open_second_file :
    lines = lines.strip()
    if len(lines) < 1 : 
        continue
    for letter in lines :
        if letter.isalpha() :
            letter = letter.lower()
            second_hash[letter] = second_hash.get(letter, 0) + 1

print('First file: ', first_hash)
print('Second file: ', second_hash)