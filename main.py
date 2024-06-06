print("\nWelcome. Let's determine if the ransom note was created with a specific magazine.\n")

# Initialize dictionaries to store character counts
ransom_note_hash = dict ()
magazine_hash = dict ()

# Function to read through file and count letter
def read_file_count_letters(filename) :
    letter_count = dict ()
    for lines in filename :
        lines = lines.strip()
        for letter in lines :
            if letter.isalpha() :
                letter = letter.lower()
                letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

# Function to determine if the ransom note can be constructed from the magazine letters
def can_construct_ransom_note_from_magazine(ransom_note_hash, magazine_hash) :
    for letter, count in ransom_note_hash.items () :
        if letter in magazine_hash and ransom_note_hash[letter] > magazine_hash[letter]:
            return False, letter, ransom_note_hash[letter], magazine_hash[letter]
    return True, None, None, None

# Prompt user for the first file name and handle errors

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

# Initialize function to count characters in files and map to dictionaries
letter_count = read_file_count_letters(open_ransom_note)
ransom_note_hash.update(letter_count)

letter_count = read_file_count_letters(open_magazine)
magazine_hash.update(letter_count)

# Initialize function to compare character counts in files
can_construct, missing_letter, ransom_count, magazine_count = can_construct_ransom_note_from_magazine(ransom_note_hash, magazine_hash)

# Print results of comparison of ransom note and magazine
if can_construct == True :
    print('TRUE: the ransom note may have been created with this magazine.')
else :
    print("FALSE: the ransom note was not created with this magazine.\n", 
          missing_letter, "appears in the ransom note", ransom_count, 
          "times, and only appears in the magazine", magazine_count, "times.")