""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg - a website devoted to making books that have entered the
public domain available to anyone.
In this project, I use the novel Huckleberry Finn to figure analyze word
frequency.

The runtime for my computer is about 16 seconds.

@author = Colvin Chapman
"""

import string
import time
huck = 'pg32325.txt'


def trim_string(st):
    """turns string into more managable format.
    >>> trim_string('SGHsdg.14!\n')
    'sghsdg'
        """
    exclude = set(string.punctuation+string.digits+'ÉÈÀÂ“”﻿')
    st = ''.join(ch for ch in st if ch not in exclude)
    return st


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """

    fin = open(file_name, 'r')
    whole_string = fin.read()
    whole_string = whole_string.lower()
    novel_start = 5414
    novel_end = 606792
    st = whole_string[novel_start: novel_end]  # trimming off the extra text
    trimmed = trim_string(st)
    # accountung for line breaks up to 3 blank lines, and 2 spaces together
    trimmed = trimmed.replace('\n\n\n', ' ')
    trimmed = trimmed.replace('\n\n', ' ')
    trimmed = trimmed.replace('\n', ' ')
    trimmed = trimmed.replace('  ', ' ')
    words_split = trimmed.split(' ')
    return words_split


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentpasslyoccurring
    """
    # Create histogram in a dictionary
    word_count = {}
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1

    # reformat dictionary into a list of tuples and sorts
    word_pairs = []
    for word in word_count:
        word_pairs.append((word_count[word], word))
        smalls = sorted(word_pairs)

    # order correctly, and limit to n words
    larges = []
    for p in range(n):
        larges.append(smalls[-p-1])

    common_words = []
    for pair in larges:
        common_words.append(pair[1])
    return common_words


def word_frequency(file_name, n):
    """
    Calls previous parts to get the word list, and return the n most common
    words in that word_list
        """
    word_list = get_word_list(huck)
    return get_top_n_words(word_list, n)


if __name__ == "__main__":
    start = time.time()
    print(word_frequency(huck, 100))
    print('The runtime was %f seconds.' % (time.time()-start))
