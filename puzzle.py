def check_digits(board: list[str]) -> bool:
    """
    The function do check if elem in list have more than one similar digt
    :param board: board of game
    :return: bool
    >>> check_digits([ "**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 "," 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    for i in board:
        i = i.replace('*', '')
        for k in i:
            if i.count(k) > 1:
                return False
    return True

