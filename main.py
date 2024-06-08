import argparse

# Prompt for Filename
def input_filename(files):
    file_handles = {}
    for item in files:
        while True:
            handle = input(f'Enter the file name of the {item}: ')
            try:
                with open(handle, 'r') as open_file:
                    print(f'file opened: {handle}')
                    file_handles[item] = open_file.read()
                break  # Break the inner loop once the file is successfully read
            except FileNotFoundError:
                print(f'File {handle} cannot be opened. Try again.')
            except Exception as e:
                print(f'An unexpected error occurred: {e}')
                break  # Optionally break the loop on other exceptions to prevent infinite looping
    return file_handles

# Files to request from user
files = ['ransom note', 'magazine']

# Handle string input from terminal or prompt for filename
def read_files () :
    parser = argparse.ArgumentParser(description='Read a string from a terminal or prompt user for a text file.')
    parser.add_argument('--ransom', type=str, help='Input string for the ransom note')
    parser.add_argument('--magazine', type=str, help='Input string for the magazine')

    args = parser.parse_args()

    if args.ransom and args.magazine :
        open_ransom_note = args.ransom
        open_magazine = args.magazine
    else :
        file_contents = input_filename(files)
        open_ransom_note = file_contents['ransom note']
        open_magazine = file_contents['magazine']

    return open_ransom_note, open_magazine

# Read through file and count letter
def read_file_count_letters(filename) :
    letter_count = dict ()
    for lines in filename :
        lines = lines.strip()
        for letter in lines :
            if letter.isalpha() :
                letter = letter.lower()
                letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

# Determine if the ransom note can be constructed from the magazine letters
def can_construct_ransom_note_from_magazine(ransom_note_hash, magazine_hash) :
    for ransom_letter, ransom_count in ransom_note_hash.items():
        if ransom_letter not in magazine_hash or ransom_count > magazine_hash.get(ransom_letter, 0):
            return False, ransom_letter, ransom_count, magazine_hash.get(ransom_letter, 0)
    return True, None, None, None

# Initialize dictionaries to store character counts
ransom_note_hash = dict ()
magazine_hash = dict ()

# Run program
if __name__ == "__main__":
    print("\nWelcome. Let's determine if the ransom note was created with a specific magazine.\n")

    # Prompt user for the first file name and handle errors
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
        print('TRUE: the ransom note may have been created with this magazine.\n')
    elif can_construct == False and ransom_count == 1 :
        print(f"FALSE: the ransom note was not created with this magazine.\n\n" 
          f"'{missing_letter}' appears in the ransom note {ransom_count} " 
          f"time, and only appears in the magazine {magazine_count} times.\n")
    elif can_construct == False and magazine_count == 1 :
        print(f"FALSE: the ransom note was not created with this magazine.\n\n" 
          f"'{missing_letter}' appears in the ransom note {ransom_count} " 
          f"times, and only appears in the magazine {magazine_count} time.\n")
    else :
        print(f"FALSE: the ransom note was not created with this magazine.\n\n" 
          f"'{missing_letter}' appears in the ransom note {ransom_count} " 
          f"times, and only appears in the magazine {magazine_count} times.\n")