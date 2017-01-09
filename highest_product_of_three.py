def highest_product_of_three(my_list):
    """returns highest product of three numbers in a list

    >>> highest_product_of_three([1, 2, 3])
    6

    >>> highest_product_of_three([0, 2, 3])
    0

    >>> highest_product_of_three([1, 2, 3, 4])
    24

    >>> highest_product_of_three([1, 10, -5, 1, -100])
    5000

    """
    max_product_of_three = my_list[0] * my_list[1] * my_list[2]
    max_product_of_two = my_list[0] * my_list[1]
    min_product_of_two = my_list[0] * my_list[1]
    lowest_num = my_list[0]
    highest_num = my_list[0]


    for num in my_list:
        max_product_of_three = max(max_product_of_three, min_product_of_two * num, max_product_of_two * num)
        max_product_of_two = max(max_product_of_two, highest_num * num, lowest_num * num)
        min_product_of_two = min(min_product_of_two, highest_num * num, lowest_num * num)
        lowest_num = min(lowest_num, num)
        highest_num = max(highest_num, num)


    
    return max_product_of_three



if __name__ == "__main__":
    import doctest
    doctest.testmod()