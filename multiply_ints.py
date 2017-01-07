def multiply_ints(list_of_ints):
    """multiplies a list of ints by all ints in list but the int at that index

    >>> multiply_ints([1, 7, 3, 4])
    [84, 12, 28, 21]

    """
    products_of_all_ints_before_ind = [None] * len(list_of_ints)
    preproduct = 1
    
    for idx, num in enumerate(list_of_ints):
        products_of_all_ints_before_ind[idx] = preproduct
        preproduct *= num


    products_of_all_ints_after_ind = [None] * len(list_of_ints)
    postproduct = 1

    for idx in xrange(len(list_of_ints) - 1, -1, -1):
        products_of_all_ints_after_ind[idx] = postproduct
        postproduct *= list_of_ints[idx]

    return products_of_all_ints_after_ind



if __name__ == "__main__":
    import doctest
    doctest.testmod()
