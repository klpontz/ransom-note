# LETTER FREQUENCY COMPARISON

**Scenario**: You have a ransom note. It was made from the clippings of a magazine. You need to determine if the ransom note was made with a specific magazine. 

The solution should return an answer to the question: could the ransom note have been created from this magazine?

## To Run Program

Download the files to your computer. Open your terminal and change directories to where you saved the files. Run the following command:

`python3 main.py`

You will be prompted to enter the name of two files to compare. The first prompt is for the ransom note and the second prompt is for the magazine.

There is also an option to input a string for the ransom note and magazine in the command line. Use the following command to do so:

`python3 main.py --ransom "Give me all the money" --magazine "Wow, look at all of this money laying around"`

The previous command returns the following results:

```
FALSE: the ransom note was not created with this magazine.

'g' appears in the ransom note 1 times, and only appears in the magazine 0 times.
```