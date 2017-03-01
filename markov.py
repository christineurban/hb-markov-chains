from random import choice
#from random method import choice 
#choice will randomize word from list below


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    
    return contents

# open_and_read_file("green-eggs.txt")


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()
    #splits the text string into individual words in list
    #split will return a list, always
    words.append(None)
    #append None to words list becuase it's a marker to stop. Terminate.

    for i in range(len(words)-2):
        #for index in range of the length of words -2 to allow for 3 variables 
        #in the end

        bi_gram = (words[i], words[i + 1])
        # makes key, which is a tuple of a word and the next consecutive word
        
        chains[bi_gram] = chains.get(bi_gram, [])
        # a["berry"] = a.get("berry", [])
        # will check for existence of bi_gram key, and if it doesn't exist, 
        # add it as key + empty string as value

        chains[bi_gram].append(words[i + 2])
        #will append a possible consecutive word.

        # chains[bi_gram] is REPRESENTING the value. So we are appending to
        # the value which is a LIST. Therefore you can append to it!
   
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    bi_gram = choice(chains.keys())
    first, second = bi_gram
    third = choice(chains[bi_gram])


    text += first + " " + second


    while third:
        text += " " + third
        bi_gram = (second, third)
        first, second = bi_gram
        third = choice(chains[bi_gram])

    return text



input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
