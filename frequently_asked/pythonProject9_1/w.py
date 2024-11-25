#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getSearchResults' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY words
#  2. STRING_ARRAY queries
#

def getSearchResults(words, queries):
    # Write your code here
    n = []
    print(words, queries)
    x = [sorted(x) for x in words]
    for item in queries:
        for item2 in x:
            if sorted(item) == item2:
                print(item2)
                n.append(item2)
    return n


if __name__ == '__main__':

    fptr = open("w.txt", 'w')

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    result = getSearchResults(words, queries)

    fptr.write('\n'.join([' '.join(x) for x in result]))
    fptr.write('\n')

    fptr.close()
