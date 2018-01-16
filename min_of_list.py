def get_min(numbers):
    """ Return a new list with the smallest value in the input list.
    Before returning the new list, remove the value from the original list.

    >>> nums = [3, 4, 1]
    >>> get_min(nums)
    >>> [1]
    >>> nums
    >>> [3, 4]
    """

    # your code here
    min_n = min(numbers)
    temp_lst = numbers[:]
    for i in range(len(temp_lst)):
        if temp_lst[i] == min_n:
            numbers.pop(i)
    # numbers.remove(min_n)
    return [min_n]