def multiply_ints(list_of_ints):
    """multiplies a list of ints by all ints in list but the int at that index

    >>> multiply_ints([1, 7, 3, 4])
    [84, 12, 28, 21]

    """

    totals = [1 for num in list_of_ints]
    for ind, num in enumerate(list_of_ints):
        for m, multiplier in enumerate(list_of_ints):
            if m != ind:
                totals[ind] *= multiplier 
    return totals

if __name__ == "__main__":
    import doctest
    doctest.testmod()
