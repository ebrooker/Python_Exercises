"""
Ezra S. Brooker

2021-08-02

Daily Coding Problem

Compute the running median of a sequence of numbers. That is, given a stream of
numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two
middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should
print out: 2, 1.5, 2, 3.5, 2, 2, 2

"""

from bisect import insort as bisect_insort


def running_median(numbers):

    ordered = []
    for i,n in enumerate(numbers):
        bisect_insort(ordered,n)

        j = i//2

        if i % 2 == 0:
            # Odd number list length
            print(f"{ordered[j]}")

        else:
            # Even number list length
            median = 0.5 * (ordered[j] + ordered[j+1])
            print(f"{median}")


if __name__ == "__main__":

    nums = [2, 1, 5, 7, 2, 0, 5]

    running_median(nums)

