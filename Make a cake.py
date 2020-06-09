N = int(input())
A = list(map(int, input().split()))
for j in A:
    if j == max(A):
        print(j)
    else:
        print()
for i in range(1, N+1):
    if N.index(max(A)-i) < N.index(max(A)):
        print(max(A)-i)
        