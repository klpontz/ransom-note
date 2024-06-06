# Prompt user for the first file name and handle errors

print("\nWelcome. Let's determine if the ransom note was created with this magazine.\n")

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

def can_construct_ransom_note_from_magazine(ransom_note_hash, magazine_hash) :
    for letter, count in ransom_note_hash.items () :
        if letter in magazine_hash and ransom_note_hash[letter] > magazine_hash[letter]:
            return False, letter, ransom_note_hash[letter], magazine_hash[letter]
    return True, None, None, None

can_construct, missing_letter, ransom_count, magazine_count = can_construct_ransom_note_from_magazine(ransom_note_hash, magazine_hash)

if can_construct == True :
    print('TRUE: the ransom note may have been created with this magazine.')
else :
    print("FALSE: the ransom note was not created with this magazine.\n", 
          missing_letter, "appears in the ransom note", ransom_count, 
          "times, and only appears in the magazine", magazine_count, "times.")