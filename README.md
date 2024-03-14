# Reading-Files
There are five methods to be used when processing text files. 

The first method count_words counts how many times every word appears in a text file. 
Then creates a dictionary to store each word along with the number of times each word appears in the file

There are some common words that we don’t want to include in our dictionary. These
words are provided in a set called stop_words. 
Words that are in the stop_words are not included in the dictionary results.

find_max finds the word in the dictionary that has the maximum count and returns it in a tuple

find_same_words and find_different_words can be called on two text files to find words that are 
shared, and words that are different respectively. 

In the driver code I'm using the text files raven.txt and road.txt
These files are inlcuded in this repo and hardcoded into the driver code.
For implementation simply change the name of the text files which you would like to read in.

print_word_count takes in the created dictionary and a word for which to print the associated count
Make sure you change the word when calling on a new text file. 
