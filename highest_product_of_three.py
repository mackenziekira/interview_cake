def highest_product_of_three(my_list):
    """returns highest product of three numbers in a list

    >>> highest_product_of_three([1, 2, 3])
    6

    >>> highest_product_of_three([0, 2, 3])
    0

    >>> highest_product_of_three([1, 2, 3, 4])
    24

    """
    max_product = None

    for x in xrange(len(my_list) - 2):
        for y in xrange(1, len(my_list) - 1):
            for z in xrange(2, len(my_list)):
                if x * y * z > max_product:
                    max_product = x * y * z
    return max_product



if __name__ == "__main__":
    import doctest
    doctest.testmod()