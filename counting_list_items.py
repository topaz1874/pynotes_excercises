# Create a function that returns a dictionary of the items of a list
# and their counts.

def count_items(lst):    
    """ Return counts of the list items.
    
    >>> count_items(['one', 'two', 'two', 'three', 'three', 'three'])
    >>> {'one': 1, 'three': 3, 'two': 2}
    """

    # your code here
    lst.sort()
    lst_dict = {}
    keys = set(lst)
    for key in keys:
        lst_dict[key] = lst.count(key)
    # lst_dict = {item: lst.count(item) for item in lst}
    return lst_dict