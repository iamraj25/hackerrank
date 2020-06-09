# from numpy.core import long
#
# K, M = [int(x) for x in input().split()]
# list1 = []
# list2 = []
# for _ in range(K):
#     list1.append([int(x) for x in input().split()])
# # print(list1)
# for i in range(K):
#     list2.append(long(max(list1[i])**2))
# # print(list2)
# sum = sum(list2) % M
# print(sum)


# import itertools
#
# from pip._vendor.distlib.compat import raw_input
#
# (K, N) = map(int, raw_input().split())
#
# L = []
# for i in range(K):
#     l = map(int, raw_input().split())
#     n = l[0]
#     L.append(l[1:])
#     assert len(L[i]) == n
#
# S_max = 0
# L_max = None
#
# for l in itertools.product(*L):
#     s = sum([x**2 for x in l]) % N
#
#     if s > S_max:
#         S_max = s
#         L_max = l
#
# print(S_max)
from pip._vendor.distlib.compat import raw_input

n=list(map(int,raw_input().split()))
l=n[0]
div=n[1]
b=list()
for i in range(0,l):
    a=list()
    a.extend(map(int,raw_input().split()))
    b.append(max(a))
    su=0
for j in b:
    su+=j*j

print(su%div)