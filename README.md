# Letter Frequency Comparison

**Scenario**: You have a ransom note. It was made from the clippings of a magazine. You need to determine if the ransom note was made with a specific magazine. 

This program will handle this scenario by counting the frequency of letters in the ransom note and compare the frequency of letters in the magazine. If there are more of one letter in the ransom note than in the magazine, the ransom note could not have been created by the magazine. But if the magazine contains more letters than the ransom note, the ransom note could have been created with the magazine. 

## To Run Program

Download the files to your computer. Open your terminal and change directories to where you saved the files. Run the following command:

`python3 main.py`

You will be prompted to enter the name of two files to compare. The first prompt is for the ransom note and the second prompt is for the magazine.

There is also an option to input a string for the ransom note and magazine in the command line. Use the following command to do so:

`python3 main.py --ransom "Give me all the money" --magazine "Wow, look at all of this money laying around"`

The previous command returns the following results:

```
FALSE: the ransom note was not created with this magazine.

A Mismatching Letter: 'v'
Count in Ransom Note: 1
Count in Magazine: 0
```

## Make it More Real

To take this scenario seriously, we would not read in a text file. A ransom note is unique not just because of the letters. There's more to account for: font style, font size, font family, and more. For a real world scenario, we should create a program that reads in the images of the ransom note and the magazine. The program would need to create a shape around the letters matching the shapes in the ransome note and record the pixel values in a matrix. Now we can compare the collection created from the ransom note against the collection created from the magazine. This would give us the best chance of knowing if a ransom note was created from a specific magazine.