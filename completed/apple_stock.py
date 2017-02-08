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

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for ind, price in enumerate(stock_prices_yesterday):
        if ind == 0:
            continue

        current_profit = price - min_price

        min_price = min(min_price, price)

        max_profit = max(max_profit, current_profit)

    return max_profit


if __name__ == "__main__":
    import doctest
    doctest.testmod()