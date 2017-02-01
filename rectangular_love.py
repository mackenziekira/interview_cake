def rectangular_love(rect1, rect2):
    """
    >>> rectangular_love( {'left_x': 1, 'bottom_y': 5, 'width': 10, 'height': 4}, {'left_x': 0, 'bottom_y': 0, 'width': 2, 'height': 6}) == {'left_x': 1, 'bottom_y': 5, 'width': 1, 'height': 1}
    True

    >>> rectangular_love( {'left_x': 0, 'bottom_y': 0, 'width': 1, 'height': 1}, {'left_x': 5, 'bottom_y': 5, 'width': 2, 'height': 6}) == {'left_x': None, 'bottom_y': None, 'width': None, 'height': None}
    True

    >>> rectangular_love( {'left_x': 0, 'bottom_y': 0, 'width': 10, 'height': 10}, {'left_x': 2, 'bottom_y': 2, 'width': 2, 'height': 3}) == {'left_x': 2, 'bottom_y': 2, 'width': 2, 'height': 3}
    True

    """
    result = {}

    x = find_overlap({'lower_coordinate': rect1['left_x'], 'extent': rect1['width']}, {'lower_coordinate': rect2['left_x'], 'extent': rect2['width']})

    result['left_x'], result['width'] = x['lower_coordinate'], x['extent']

    y = find_overlap({'lower_coordinate': rect1['bottom_y'], 'extent': rect1['height']}, {'lower_coordinate': rect2['bottom_y'], 'extent': rect2['height']})

    result['bottom_y'], result['height'] = y['lower_coordinate'], y['extent']

    return result

def find_overlap(line1, line2):
    """
    >>> find_overlap({'lower_coordinate': 1, 'extent': 10}, {'lower_coordinate': 0, 'extent': 2})
    {'lower_coordinate': 1, 'extent': 1}

    >>> find_overlap({'lower_coordinate': 5, 'extent': 4}, {'lower_coordinate': 0, 'extent': 6})
    {'lower_coordinate': 5, 'extent': 1}
    """
    highest_start_of_overlap = max(line1['lower_coordinate'], line2['lower_coordinate'])
    line1_higher_coordinate = sum(line1.values())
    line2_higher_coordinate = sum(line2.values())
    lowest_end_of_overlap = min(line1_higher_coordinate, line2_higher_coordinate)

    if highest_start_of_overlap >= lowest_end_of_overlap:
        return {'lower_coordinate': None, 'extent': None}
    else:
        return {'lower_coordinate': highest_start_of_overlap, 'extent': lowest_end_of_overlap - highest_start_of_overlap}



if __name__ == "__main__":
    import doctest
    doctest.testmod()