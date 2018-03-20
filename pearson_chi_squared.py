# Daniel Shats

from nltk.corpus import brown
import nltk
import numpy as np
import re

def chi_square(w1, w2, corpus):

    words = [w.lower() for w in corpus.words()]
    bigrams = list(nltk.bigrams(words))

    c_w1 = words.count(w1)
    c_w2 = words.count(w2)
    print('C(w1):\t\t\t', c_w1)
    print('C(w2):\t\t\t', c_w2)

    c_w1_w2 = bigrams.count((w1,w2))
    print('C(w1w2):\t\t', c_w1_w2)

    c_w1_not_w2 = c_w1 - c_w1_w2
    print('C(w1 && !w2):\t\t', c_w1_not_w2)

    c_not_w1_w2 = c_w2 - c_w1_w2
    print('C(!w1 && w2):\t\t', c_not_w1_w2)

    c_neither = len(bigrams) - c_w1_w2
    print('C(!w1 && !w2):\t\t', c_neither)

    N = np.sum([c_w1_w2, c_not_w1_w2, c_w1_not_w2, c_neither ])

    print('Total Words (N):\t', N)
    print()
    print('0.05% Baseline:\t\t', '3.841')

    #construct Observed value matrix:
    observed = np.reshape([c_w1_w2, c_not_w1_w2, c_w1_not_w2, c_neither ], (2,2))

    # construct Expected value matrix:
    e00 = (np.sum(observed[0][:]) * np.sum(observed[0:2,0]))/N
    e10 = (np.sum(observed[1][:]) * np.sum(observed[0:2,0]))/N
    e01 = (np.sum(observed[0][:]) * np.sum(observed[0:2,1]))/N
    e11 = (np.sum(observed[1][:]) * np.sum(observed[0:2,1]))/N
    expected = np.reshape([e00, e01, e10, e11], (2,2))



    # calculate x^2:
    chi_sq = 0
    for row in range(2):
        for col in range(2):
            chi_sq += ((observed[row][col]-expected[row][col])**2)/(expected[row][col])
    print('X^2:\t\t\t', chi_sq)

    print()

    print('We do not have a collocation') if chi_sq < 3.814 else print('We have a collocation')

if __name__ == '__main__':

    chi_square('new', 'companies', brown)
