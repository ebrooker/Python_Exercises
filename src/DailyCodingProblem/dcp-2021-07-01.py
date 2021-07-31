"""
Ezra S. Brooker

2021-07-01

Daily Coding Problem

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""


def sum_exists(numbers, k):
    return any(True if k-n in numbers else False for n in numbers)


if __name__ == "__main__":

    n = [10, 15, 3, 7]
    k = 17

    print(sum_exists(n,k))

    n[-1] = 6
    print(sum_exists(n,k))

    n = [3, 6, 1, 2]
    k = 9
    print(sum_exists(n,k))

    k = 8
    print(sum_exists(n,k))

    n[-1] = 3
    print(sum_exists(n,k))

    n = [6, 2, 5, 3]
    print(sum_exists(n,k))

