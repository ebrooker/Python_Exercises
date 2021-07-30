"""
Ezra S. Brooker

2021-07-29

Daily Coding Problem

Run-length encoding and decoding of alpha, non-numeric strings.

"""


def encode(string):

    counter = 1
    encoded_str = ""
    string = string+" "
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            counter+=1
        else:
            encoded_str+=f"{counter}{string[i]}"
            counter = 1

    return encoded_str


def decode(string):

    decoded_str = "".join(int(string[i])*string[i+1] for i in range(0,len(string),2))

    return decoded_str


if __name__ == "__main__":

    test_str = "AAAABBBCCDAA"

    enc = encode(test_str)
    dec = decode(enc)

    print(enc)
    print(dec)