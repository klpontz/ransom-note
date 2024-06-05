# Prompt user for the first file name and handle errors

print("\nWelcome. Let's determine if the ransom note was created with this magazine.\n")

while True :
    first_fhandle = input('Enter the file name of the ransom note: ')
    try:
        open_ransom_note = open(first_fhandle)
        break
    except:
        print('File', first_fhandle, 'cannot be opened. Try again.')

# Prompt user for the second file name and handle errors
while True :
    second_fhandle = input('Enter the file name for the magazine: ')
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

# Compare values in rasome note to values in magazine
for key in ransom_note_hash :
    if key in magazine_hash and ransom_note_hash[key] > magazine_hash[key] :
        print("False: the ransom note was not created with this magazine.\n", key, "appears in the ransom note", ransom_note_hash[key], "times, and only appears in the magazine", magazine_hash[key], "times.")
        break
    print('True: the ransom note could have been created with this magazine.')