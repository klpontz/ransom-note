import argparse

# Create parser to handle string input from terminal
def read_files () :
    parser = argparse.ArgumentParser(description='Read a string from a terminal or prompt user for a text file.')
    parser.add_argument('--ransom', type=str, help='Input string for the ransom note')
    parser.add_argument('--magazine', type=str, help='Input string for the magazine')

    args = parser.parse_args()

    if args.ransom and args.magazine :
        open_ransom_note = args.ransom
        open_magazine = args.magazine
    
    else :
        while True :
            first_fhandle = input('Enter the file name of the ransom note: ')
            try:
                open_ransom_note = open(first_fhandle)            
                break
            except:
                print('File', first_fhandle, 'cannot be opened. Try again.')

        while True :
            second_fhandle = input('Enter the file name for the magazine: ')
            try:
                open_magazine = open(second_fhandle)
                break
            except:
                print('File', second_fhandle, 'cannot be opened. Try again.')

    return open_ransom_note, open_magazine

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
    for ransom_letter, ransom_count in ransom_note_hash.items () :
        for magazine_letter, magazine_count in magazine_hash.items () :
            if ransom_letter not in magazine_hash or ransom_count > magazine_count :
                return False, magazine_letter, ransom_count, magazine_count
    return True, None, None, None

# Initialize dictionaries to store character counts
ransom_note_hash = dict ()
magazine_hash = dict ()

# Prompt user for the first file name and handle errors
print("\nWelcome. Let's determine if the ransom note was created with a specific magazine.\n")

open_ransom_note, open_magazine = read_files()

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