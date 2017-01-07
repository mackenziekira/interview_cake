def multiply_ints(list_of_ints):
    """multiplies a list of ints by all ints in list but the int at that index

    >>> multiply_ints([1, 7, 3, 4])
    [84, 12, 28, 21]

    """

    # totals = [1 for num in list_of_ints]
    # for ind, num in enumerate(list_of_ints):
    #     for m, multiplier in enumerate(list_of_ints):
    #         if m != ind:
    #             totals[ind] *= multiplier 

    pre = preproduct_tally(list_of_ints)
    post = reversed(preproduct_tally(reversed(list_of_ints)))

    return [x * y for x, y in zip(pre, post)]

def preproduct_tally(list_of_ints):
    """keeps a running tally of product preceeding each item in a list"""

    preproduct = 1
    totals = []
    for num in list_of_ints:
        totals.append(preproduct)
        preproduct *= num

    return totals

if __name__ == "__main__":
    import doctest
    doctest.testmod()
