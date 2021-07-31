"""
Ezra S. Brooker

2021-07-02

Daily Coding Problem

Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
be [2, 3, 6].

Follow-up: what if can't use division?

"""
from math import prod as math_prod
import time

def pi_except_at_i_with_div(numbers):
    # Use integer division since Python 2 is no longer supported, assume only Python 3
    return [math_prod(numbers)//n for n in numbers]


def pi_except_at_i(numbers):

    return [ math_prod(numbers[j] for j in range(len(numbers)) if j!=i) for i in range(len(numbers)) ]


if __name__ == "__main__":

    print("\nPI operator excluding index i w/ division")
    n = [1, 2, 3, 4, 5]
    ti0 = time.perf_counter()
    print(pi_except_at_i_with_div(n))
    tf0 = time.perf_counter() - ti0

    n = [3, 2, 1]
    ti1 = time.perf_counter()
    print(pi_except_at_i_with_div(n))
    tf1 = time.perf_counter() - ti1

    print("\nPI operator excluding index i w/o division")
    n = [1, 2, 3, 4, 5]
    ti2 = time.perf_counter()
    print(pi_except_at_i(n))
    tf2 = time.perf_counter() - ti2

    n = [3, 2, 1]
    ti3 = time.perf_counter()
    print(pi_except_at_i(n))
    tf3 = time.perf_counter() - ti3

    print("\nTimings")
    print(f"\n{tf0}\n{tf1}\n{tf2}\n{tf3}\n")