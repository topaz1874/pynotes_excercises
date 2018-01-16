# Use regex to eliminate whitespace(s) between two specific words
import re

def remove_spaces(text, word_one, word_two):
    """ Return text after removing whitespace(s) between two specific words.
    
    >>> remove_spaces("an app store app maker app    store", "app", "store")
    >>> 'an appstore app maker appstore'
    """

    # your code here
    p = re.compile(word_one+'\s+'+word_two)
    # p = re.compile(r'{}\s+{}'.format(word_one, word_two))
    repl = word_one + word_two
    result = p.sub(repl, text)
    return result