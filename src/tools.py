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