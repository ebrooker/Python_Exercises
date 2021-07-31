"""
Ezra S. Brooker

2021-07-29

Daily Coding Problem

Given a string of round, curly, and square open and closing brackets, return 
whether the brackets are balanced (well-formed).

For examples, given the string "([])[]({})", you should return True.

Given the string "([)]" or "((()", you should return False.

"""


def is_balanced(string):

    


def balance_init(string):

    if len(string) % 2 != 0:
        return False
    
    elif string[0] in ")}]":
        return False
    
    elif string[-1] in "({[":
        return False

    else:
        return is_balanced(string)


def case_0():

    string = "([])[]({})"
    print(balance_init(string))


def case_1():

    string = "([)]"
    print(balance_init(string))


def case_2():

    string = "((()"
    print(balance_init(string))


if __name__ == "__main__":

    case_0()
    case_1()
    case_2()