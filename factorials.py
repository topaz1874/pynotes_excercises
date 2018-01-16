# Find factorials of a list of numbers

def factorialize(numbers):
    """ Return factorials of a list of numbers.
    
    >>> factorialize([1, 2, 3, 4, 5])
    >>> [1, 2, 6, 24, 120]
    """

    # your code here
    fact_list = []

    for i in range(len(numbers)):
        fact_num = 1
        for num in numbers[:i+1]:
            fact_num *= num
        fact_list.append(fact_num)
    # answers
    # from math import factorial
    # return [factorial(num) for num in numbers]
    return fact_list 