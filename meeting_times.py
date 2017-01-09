def meeting_times(list_of_meeting_times):
    """returns list of tuples of all times people are in meetings.

    >>> meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]

    >>> meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]
    """

    list_of_meeting_times.sort()

    merged_meetings = []

    for idx, current_meeting in enumerate(list_of_meeting_times):
        if idx < len(list_of_meeting_times) - 1:

            next_meeting = list_of_meeting_times[idx + 1]
            if next_meeting[0] <= current_meeting[1]:
                if next_meeting[1] > current_meeting[1]:
                    next_meeting = (current_meeting[0], next_meeting[1])
                else:
                    next_meeting = (current_meeting[0], current_meeting[1])
                list_of_meeting_times[idx + 1] = next_meeting
            else:
                merged_meetings.append(current_meeting)
        else:
            merged_meetings.append(current_meeting)

    return merged_meetings


if __name__ == "__main__":
    import doctest
    doctest.testmod()