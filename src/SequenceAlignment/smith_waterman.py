"""

Ezra S. Brooker

2021-08-02

Smith-Waterman algorithm for sequence alignment with DNA
sequences.

Uses a simple substitution matrix for DNA bases, A,C,G,T where matches are
given a score of +3 and mismatches are given a score of -3

Uses a simple constant gap penalty where gaps are given a score of -2

Finally, there is a traceback algorithm implemented to recover the aligned
strings of the two sequences being compared.

Makes use of the numpy module for efficient array indexing and filling.

"""
import numpy as np


ZERO = 0


def substitution_matrix(a,b):

    """ Simple subsitution matrix, matches are +1, mismatches are -1 """

    if a == b:
        return 3
    else:
        return -3


def constant_penalty():
    return -2


def traceback(seq_a,seq_b,score):
    """ Get traceback(s) of DNA string alignments """

    imaxes,jmaxes = np.where(score == score.max())
    traces_a, traces_b = [], []
    print(score)
    for k in range(imaxes.size):
        imax,jmax = imaxes[k], jmaxes[k]
        trace_a, trace_b = "", ""
        
        while True:

            near  = [score[imax-1,jmax-1], score[imax,jmax-1], score[imax-1,jmax]]
            inear = np.argmax(near)

            if near[0] == 0:
                trace_a+=seq_a[imax-1]
                trace_b+=seq_b[jmax-1]
                break

            if inear == 0:
                imax-=1
                jmax-=1
                trace_a+=seq_a[imax]
                trace_b+=seq_b[jmax]

            elif inear == 1:
                jmax-=1
                trace_a+='-'
                trace_b+=seq_b[jmax]

            else:
                imax-=1
                trace_a+=seq_a[imax]
                trace_b+='-'

        traces_a.append(trace_a[::-1])
        traces_b.append(trace_b[::-1])

    return traces_a, traces_b


def smith_waterman(seq_a, seq_b, substitution, gap_penalty):

    na    = len(seq_a) + 1
    nb    = len(seq_b) + 1
    score = np.zeros((na,nb), dtype=np.int64)

    for i in range(1,na):
        for j in range(1,nb):
            sub = score[i-1,j-1] + substitution(seq_a[i-1],seq_b[j-1])
            gpi = score[i-1,j  ] + gap_penalty()
            gpj = score[i,  j-1] + gap_penalty()
            score[i,j] = max(ZERO, sub, gpi, gpj)

    return traceback(seq_a, seq_b, score)


def case_0():

    seq_a = "GGTTGACTA"
    seq_b = "TGTTACGG"
    trc_a, trc_b = smith_waterman(seq_a,seq_b,substitution_matrix,constant_penalty)
    print(f"\n{seq_a=}\n{seq_b=}")
    print(f"{trc_a=}\n{trc_b=}\n")


def case_1():

    seq_a= "GGTTGACTA"
    seq_b= "TTGTTACGG"
    trc_a, trc_b = smith_waterman(seq_a,seq_b,substitution_matrix,constant_penalty)
    print(f"\n{seq_a=}\n{seq_b=}")
    print(f"{trc_a=}\n{trc_b=}\n")


def case_2():

    seq_a = "GGTTGGACTA"
    seq_b = "TGTTACGG"
    trc_a, trc_b = smith_waterman(seq_a,seq_b,substitution_matrix,constant_penalty)
    print(f"\n{seq_a=}\n{seq_b=}")
    print(f"{trc_a=}\n{trc_b=}\n")


def case_3():

    seq_a = "GGTTGACTA"
    seq_b = "GGTTACGG"
    trc_a, trc_b = smith_waterman(seq_a,seq_b,substitution_matrix,constant_penalty)
    print(f"\n{seq_a=}\n{seq_b=}")
    print(f"{trc_a=}\n{trc_b=}\n")


def case_4():

    seq_a = "GGTTGTTTACTA"
    seq_b = "TGTTACGG"
    trc_a, trc_b = smith_waterman(seq_a,seq_b,substitution_matrix,constant_penalty)
    print(f"\n{seq_a=}\n{seq_b=}")
    print(f"{trc_a=}\n{trc_b=}\n")


if __name__ == "__main__":

    case_0()
    case_1()
    case_2()
    case_3()
    case_4()
