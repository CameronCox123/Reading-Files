# File: File Processing
# Author: Cameron Cox
# UT EID: cpc2526
# Course: cs303E

# Description of program: 
# Uses functions to read through text files and count the words inside then give information about said files.


from string import punctuation

# Collection of common words that we want to avoid in our counting
stop_words = {"a","am","an", "and","are", "as", "at",
              "be","but", "by", "for", "i", "if", "in", "into",
              "is", "it", "its", "my", "nor", "not", "of", "on",
              "or", "so", "than", "that", "the", "then", "this",
              "to", "too", "will", "with"}

# Strips punctuation from text files
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

#  Takes two parameters: a dictionary of words to counts and the word you would like to print the count for
def print_word_count(dictionary, word):
    print("Count of \"" + word + "\" is:", dictionary[word])



# Counts how many times every word appears in a text file
def count_words(input_file):
    """
    Reads in a .txt file and processes it to a dictionary

    :input_file: the .txt file this function reads and processes

    :word_counter: the dictionary returned. Keys hold every word in the file. Values hold the instances of each word
    """

    #processing our input_file to a list where each word is a seprate index. Removing punctuation and uppercase letters
    word_file = open(input_file, 'r')
    word_list = word_file.read()
    word_list = str.lower(word_list)
    word_list = strip_punctuation(word_list)
    word_list = word_list.split()

    word_counter = {}

    #loop through processed list of words, add it to word_counter dictionary, else increasing instance by 1
    for word in word_list:
        if word in word_counter:
            word_counter[word] = 1 + word_counter.get(word)
        else:
             word_counter[word] = 1

    #eliminate every word from set 'stop_words'
    for word in stop_words:
        if word in word_counter:
            del word_counter[word]

    word_file.close()
    return(word_counter)


# Finds the word in the dictionary that has the maximum count
def find_max(dictionary):
    """
    Reads in a dictionary and processes infromation from it to a tuple

    :dictionary: the dictionary  this function reads and processes

    :return_tuple: a tuple showing the word with the highest instance in our dictionary
    """

    #initialize variables
    max_key = ''
    max_val = 0

    #determines if the instance of a word is the highest and saves it to local variables
    for key, value in dictionary.items():
        if value > max_val:
            max_val = value
            max_key = key

    #saves variables to our tuple
    return_tuple = (max_key, max_val)
    return(return_tuple)


# Takes in two parameters, both of which are lists of words
# Returns a set of all the words that the two lists have in common.
def find_same_words(first_input, second_input):
    """
    Takes two dictionaries and determines the same words contained in both

    :first_input: first dictionary

    :second_input: second dictionary

    :shared: the words contained in both the first dictionary and second dictionary  
    """

    #set each dictionary equal to a set for easy set-processing and return
    first_set = set(first_input)
    second_set = set(second_input)
    shared = first_set & second_set

    return(shared)


# Takes in two parameters, both of which are lists of words
# Rturns a set of all the words that are in the first list, but not in the second list.]
def find_different_words(first_input, second_input):
    """
    Takes two dictionaries and determines what words are not shared in both

    :first_input: first dictionary

    :second_input: second dictionary

    :difference: the words in both dictionaries that do not appear in the other dictionary
    """

    #set each dictionary equal to a set for easy set-processing and return
    first_set = set(first_input)
    second_set = set(second_input)
    difference = first_set - second_set

    return(difference)


"""
Driver Code
"""
def main():

    # Processing files for specific words and highest instance of a word
    print_word_count((count_words('raven.txt')), find_max(count_words('raven.txt'))[0])
    print_word_count(count_words('raven.txt'), 'nevermore')
    print_word_count(count_words('raven.txt'), 'raven')

    # Printing the shared and different words between text files 
    print()
    print(find_same_words(count_words('road.txt').keys(), count_words('raven.txt').keys()))

    print()
    print(find_different_words(count_words('road.txt').keys(), count_words('raven.txt').keys()))


if __name__ == '__main__':
    main()