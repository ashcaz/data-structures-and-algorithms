def sort_func(sort_list: list) -> list:
    """[Sorts a list in place]

    Args:
        sort_list (list): [list to be sorted]

    Returns:
        list: [sorted list]
    """

    for i in range(1, len(sort_list)):
        j = i - 1
        temp = sort_list[i]

        while j >= 0 and temp < sort_list[j]:

            sort_list[j + 1] = sort_list[j]
            j = j - 1

        sort_list[j + 1] = temp

    return sort_list