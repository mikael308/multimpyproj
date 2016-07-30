from random import randint

alpha_numeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ1234567890-+/*!?&"

def get_id():

    l = len(alpha_numeric)
    id = ""
    for i in range(0, 30):
        id += alpha_numeric[randint(0, l-1)]

    return id

