"""
Question: Write a function that takes in a string of one or
more words, and returns the same string, but with all five or
more letter words reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"

This question was asked on Codewars website.

PROGRAM LOGIC
--------------------
Declare two empty lists called list_str_to_words and list_spin_words.
split the string into words on basis of spaces and save to a list_str_to_words.

Iterate over the list and count the character length of each word.
If the word length is greater than 5 then reverse the word and
write to list_spin_words
if the word length is not greater tha 5, add the word to
list_spin_words
---------------------
Created on Wed Oct  7 15:35:34 2020

@author: Ashish
"""
# declare global string variable
some_string = "Welcome"
# declare global lists
# split string into a list of words
def spin_words(some_string):
    list_str_to_words, list_spin_words = [], []
    list_str_to_words = some_string.split()
    for word in list_str_to_words:
        if(len(word) > 5):
            rev_word = "".join(reversed(word))
            list_spin_words.append(rev_word)
        else:
            list_spin_words.append(word)
    str_to_return = " ".join(list_spin_words)
    return(str_to_return)

# Invoke the function
print(spin_words(some_string))
