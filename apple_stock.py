def get_max_profit(stock_prices_yesterday):
    """returns max profit you could have made off a list of stock prices

    >>> get_max_profit([10, 7, 5, 8, 11, 9])
    6

    >>> get_max_profit([10, 7, 5, 8, 11, 9, 4])
    6

    >>> get_max_profit([10])
    'input must be a list of at least 2 or more stock prices'

    >>> get_max_profit([10, 10, 10, 10])
    0

    >>> get_max_profit([10, 9, 8, 7])
    -1

    >>> get_max_profit([])
    'input must be a list of at least 2 or more stock prices'
    """

    if not stock_prices_yesterday or len(stock_prices_yesterday) < 2:
        return 'input must be a list of at least 2 or more stock prices'

    max_price = stock_prices_yesterday[0]
    index_of_max_price = 0

    for ind, price in enumerate(stock_prices_yesterday):
        if price >= max_price:
            max_price = price
            index_of_max_price = ind

    if not index_of_max_price:
        min_price = stock_prices_yesterday[1]

        for x in xrange(1, len(stock_prices_yesterday)):
            price = stock_prices_yesterday[x]
            if price > min_price:
                min_price = price

        return min_price - max_price

    else:
        min_price = stock_prices_yesterday[0]

        for x in xrange(index_of_max_price):
            price = stock_prices_yesterday[x]
            if price < min_price:
                min_price = price

        return max_price - min_price


if __name__ == "__main__":
    import doctest
    doctest.testmod()