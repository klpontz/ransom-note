# Prompt user for the first file name and handle errors
while True :
    first_fhandle = input('Enter the file name of the ransom note: ')
    if len(first_fhandle) < 1 : first_fhandle = "ransom.txt"
    try:
        open_ransom_note = open(first_fhandle)
        break
    except:
        print('File', first_fhandle, 'cannot be opened. Try again.')

# Prompt user for the second file name and handle errors
while True :
    second_fhandle = input('Enter the file name for the magazine: ')
    if len(second_fhandle) < 1 : second_fhandle = "magazine.txt"
    try:
        open_magazine = open(second_fhandle)
        break
    except:
        print('File', second_fhandle, 'cannot be opened. Try again.')

# Initialize dictionaries to store character counts
ransom_note_hash = dict ()
magazine_hash = dict ()

# Read through the ransom note file and count characters
for lines in open_ransom_note :
    lines = lines.strip()
    if len(lines) < 1 : 
        continue
    for letter in lines :
        if letter.isalpha() :
            letter = letter.lower()    
            ransom_note_hash[letter] = ransom_note_hash.get(letter, 0) + 1

# Read through the magazine file and count characters
for lines in open_magazine :
    lines = lines.strip()
    if len(lines) < 1 : 
        continue
    for letter in lines :
        if letter.isalpha() :
            letter = letter.lower()
            magazine_hash[letter] = magazine_hash.get(letter, 0) + 1

# print('First file: ', ransom_note_hash)
# print('Second file: ', magazine_hash)

