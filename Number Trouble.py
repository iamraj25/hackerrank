from socket import *

n = int(input())
l = []

try:
    for i in range(n):
        l.append(int(input()))
    for i in sorted(l):
        print(i)
except timeout:
    print()