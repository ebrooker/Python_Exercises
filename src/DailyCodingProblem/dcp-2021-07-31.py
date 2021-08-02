"""
Ezra S. Brooker

2021-07-31

Daily Coding Problem


The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the
other. For example, the edit distance between "kitten" and "sitting" is three:
substitute the "k" for "s", substitute the "e" for "i", and append a "g".

Given two strings, compute the edit distance between them.

"""


def edit_distance(a, b, mode="Levenshtein"):

    if mode.lower() == "levenshtein":
        return Levenshtein_distance(a,b)

    else:
        return -1


def Levenshtein_distance(a,b):
    """ Allows for substitutions, insertions, and deletions """

    la, lb = len(a), len(b)

    if lb == 0:
        return la

    elif la == 0:
        return lb

    elif a[0] == b[0]:
        return Levenshtein_distance(a[1:], b[1:])

    else:

        return 1 + min(
            Levenshtein_distance(a[1:], b    ),
            Levenshtein_distance(a,     b[1:]),
            Levenshtein_distance(a[1:], b[1:])
            )


if __name__ == "__main__":

    print( edit_distance( "kitten",  "sitting" ) )
    print( edit_distance( "kitten",  "sit"     ) )
    print( edit_distance( "kitten",  "sit    " ) )
    print( edit_distance( "kitten",  "kittens" ) )
    print( edit_distance( "sitting", "sit"     ) )

