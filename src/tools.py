from random import randint


def unique_vals(n, min_val, max_val):
    """
    generates a list of unique values\n
    :param n: number of elements in list
    :param min_val: minimum value of the elements in list
    :param max_val: maximum value of the elements in list
    :return: list of unique values
    """
    if min_val > max_val:
        raise ValueError("min_val > max_val parameters not aloud")
    if n > (1 + max_val - min_val):
        raise ValueError("Not possible to produce " + str(n) + " unique values within span " + str(min_val) + ".." + str(max_val))

    vals = []
    while len(vals) < n:
        v = randint(min_val, max_val)
        if vals.count(v) == 0:
            vals.append(v)

    return vals


def divide_to_rows(max_width, text):
    """
    divide a text into rows as elements in tuple,
     the max length of each element string is param max_width.
     Wordwrap is used accept when a word exceeds the max_width.\n
    :param max_width: the maximum length of characters in each row
    :param max_width: int
    :param text: text to divide
    :type text: str
    :return:
    """
    if max_width is not int:
        ValueError("max_width argument must be int")
    rows = []
    if max_width <= 0:
        return rows
    row = ""
    rest = str(text)
    while rest is not None and len(rest) > 0:
        first, rest = sep_first_word(rest)

        if len(row + first) < max_width:
            row += first
            if rest is not None and len(row + rest) < max_width:
                rows.append(row + rest)
                break
        else:
            rows.append(row)
            row = ""
            if len(first) >= max_width:
                rows.append(first[:max_width])
                rest = first[max_width:] + rest
            else:
                rest = first + rest

    return rows


def sep_first_word(text):
    """
    separate the first word from the rest of the string\n
    :param text: the textstring to separate first word from
    :type text: str
    :return: tuple containing of first element: the first word, second element contains the rest of the text
    """
    delim = " "
    for i, c in enumerate(text):
        if delim.__contains__(c):
            i +=1
            return (text[:i], text[i:])
    return (text, "")

