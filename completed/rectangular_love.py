def rectangular_love(rect1, rect2):
    """
    >>> rectangular_love( {'left_x': 1, 'bottom_y': 5, 'width': 10, 'height': 4}, {'left_x': 0, 'bottom_y': 0, 'width': 2, 'height': 6}) == {'left_x': 1, 'bottom_y': 5, 'width': 1, 'height': 1}
    True

    >>> rectangular_love( {'left_x': 0, 'bottom_y': 0, 'width': 1, 'height': 1}, {'left_x': 5, 'bottom_y': 5, 'width': 2, 'height': 6}) == {'left_x': None, 'bottom_y': None, 'width': None, 'height': None}
    True

    >>> rectangular_love( {'left_x': 0, 'bottom_y': 0, 'width': 10, 'height': 10}, {'left_x': 2, 'bottom_y': 2, 'width': 2, 'height': 3}) == {'left_x': 2, 'bottom_y': 2, 'width': 2, 'height': 3}
    True

    >>> rectangular_love( {'left_x': 0, 'bottom_y': 0, 'width': 10, 'height': 10}, {'left_x': 10, 'bottom_y': 2, 'width': 2, 'height': 3}) == {'left_x': None, 'bottom_y': None, 'width': None, 'height': None}
    True
    """

    left_x, width = find_overlap(rect1['left_x'], rect1['width'], rect2['left_x'], rect2['width'])

    bottom_y, height = find_overlap(rect1['bottom_y'], rect1['height'], rect2['bottom_y'], rect2['height'])

    if width is None or height is None:
        return {
        'left_x': None,
        'bottom_y': None,
        'width': None,
        'height': None
        }

    return {
        'left_x': left_x,
        'bottom_y': bottom_y,
        'width': width,
        'height': height
    }

def find_overlap(lower_coord1, extent1, lower_coord2, extent2):
    """
    >>> find_overlap(1, 10, 0, 2)
    [1, 1]

    >>> find_overlap(5, 4, 0, 6)
    [5, 1]
    """
    highest_start_of_overlap = max(lower_coord1, lower_coord2)
    higher_coord1 = lower_coord1 + extent1
    higher_coord2 = lower_coord2 + extent2
    lowest_end_of_overlap = min(higher_coord1, higher_coord2)

    if highest_start_of_overlap >= lowest_end_of_overlap:
        return [None, None]
    else:
        return [highest_start_of_overlap, lowest_end_of_overlap - highest_start_of_overlap]



if __name__ == "__main__":
    import doctest
    doctest.testmod()