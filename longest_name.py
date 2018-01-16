def get_longest_name(a_list):
    """ Return '******' if the input list is [], [''], or a list containing
        names of equal length.
        Else, return the name that is greater in length than any other name
        in the list.
    
    >>> get_longest_name(["Candide", "Jessie", "Kath", "Amity", "Raeanne"])
    >>> '******'
    >>> get_longest_name(["Jessie", "Kath", "Amity", "Raeanne"])
    >>> '******'
    >>> get_longest_name(["Jessie", "Kath", "Amity"])
    >>> 'Jessie'
    """

    # your code here
    l_name = '******'

    # better solution
    """
    max_length = max([len(name) for name in a_list])
    duplicate_lengths = [name for name in a_list if len(name) == max_length]
    if not a_list:
        return l_name
    if a_list == [''] or len(duplicate_lengths) > 1:
        return l_name
    else:
        return ''.join(duplicate_lengths)
    return l_name
    """

    n_list = [(a_list[i], len(a_list[i])) for i in range(len(a_list))]
    sorted_list = sorted(n_list, key=lambda length:length[1])
    sorted_list.reverse()


    # print sorted_list
    if sorted_list:
        max_name_length = sorted_list[0][1]
        if len(sorted_list) == 1 and max_name_length > 0:
            return sorted_list[0][0]
        elif len(sorted_list) > 1 and max_name_length > sorted_list[1][1]:
            return sorted_list[0][0]
        else:
            return l_name
    else:
        return l_name