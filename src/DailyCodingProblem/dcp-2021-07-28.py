"""
Ezra S. Brooker

2021-07-28

Daily Coding Problem

Write an algorithm to justify text. Given a sequence of words and an integer
line length k, return a list of strings which represents each line, fully 
justified.

More specifically, you should have as many words as possible in each line.
There should be at leastone space between each word. Pad extra spaces when
necessary so that each line has exactly length k. Spaces should be distributed
as equally as possible, with the extra spaces, if any, distributed starting
from the left.

If you can only fit one word on a line, then you should pad the right-hand
side with spaces.

Each word is guaranteed not to be longer than k.

"""


def justify_text(words,k):

    lines = [words[0]]
    current = 0

    for word in words[1:]:
        temp_str = lines[current]

        if len(f"{temp_str} {word}") <= k:
            lines[current] = f"{temp_str} {word}"
        else:
            current+=1
            lines.append(word)

    for i in range(len(lines)):
        temp_str = lines[i]
        leftovers = k - len(temp_str)
        space_ind = [i for i,ch in enumerate(temp_str) if ch == " "]

        spaces = [1 + leftovers//len(space_ind) for i,n in enumerate(space_ind)]
        spaces = [n+1 if i+1 <= leftovers % len(space_ind) else n for i,n in enumerate(spaces)]

        temp_str = temp_str.split()
        lines[i] = "".join(f"{temp_str[i]}{spaces[i]*' '}" for i in range(len(temp_str)-1)) + temp_str[-1]

    return lines


if __name__ == "__main__":

    word_list = "the quick brown fox jumps over the lazy dog".split()

    jtext = justify_text(word_list,16)

    for line in jtext:
        print(line)

