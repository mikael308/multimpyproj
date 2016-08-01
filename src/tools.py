from random import randint


def unique_vals(n, min_val, max_val):
    """
    generates a list of unique values
    :param n: number of elements in list
    :param min_val: minimum value of the elements in list
    :param max_val: maximum value of the elements in list
    :return: list of unique values
    """
    vals = []
    while len(vals) < n:
        v = randint(min_val, max_val)
        if vals.count(v) == 0:
            vals.append(v)

    return vals