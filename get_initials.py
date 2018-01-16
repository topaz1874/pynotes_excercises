# Write a program that takes a full name, prints the initials of the first,
# middle, and last name. If the middle name is “NA”, then the program
# should print only the initials of the first and the last name.


def get_initials(name):
    """ Return initials of first, last and middle name.
    If the middle name is 'NA', return only the initials of the first and the last name.
    
    >>> get_initials("Alfred E. Newman")
    >>> 'A.E.N.'
    >>> get_initials("John NA Smith")
    >>> 'J.S.'
    """

    # your code here
    first, middle, last = name.lower().split()
    if middle == 'na':
        initials = first[0] + '.' + last[0] + '.'
    else:
        initials = first[0] + '.' + middle[0] + '.' + last[0] + '.'

    return '{}'.format(initials.upper())
