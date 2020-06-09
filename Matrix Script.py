# import math
# import os
# import random
# import re
# import sys
#
#
#
#
# first_multiple_input = input().rstrip().split()
#
# n = int(first_multiple_input[0])
#
# m = int(first_multiple_input[1])
#
# matrix = []
#
# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)
# for i in range(m):
#     for j in range(n):
#         if matrix[j][i] in "!@#$%&":
#             if matrix[j-1][i].isalnum() and matrix[j+1][i].isalnum():
#                 print("", end=" ")
#         else:
#             print(matrix[j][i], end="")


import re

from pip._vendor.distlib.compat import raw_input

n, m = map(int, raw_input().split())
a = []

for _ in range(n):
    a.append(raw_input()[:m])

s = ''.join(''.join(e) for e in zip(*a))
result = re.sub(r'([a-zA-Z0-9])([^a-zA-Z0-9]+)(?=[a-zA-Z0-9])', r'\1 ', s)
print(result)