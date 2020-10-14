# A program to compute the value of 5 card poker hands, given in the book
# "Simply Scheme", as an exercise to be done in scheme, but here I will
# impliment the same program in python.

def flush_bool(hand):
    suites = [] 
    for i in hand:
        suites.append(i[0])

    return suites
