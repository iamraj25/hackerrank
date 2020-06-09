N = int(input())
S = list(map(int, input().split(" ")))
lis = []
pac = 0
while len(S)>3:
    for i in range(N-1):
        if S[i] < S[i+1]:
            if S[i] in lis:
                pass
            else:
                lis.append(S[i])

        if len(lis) == 3:
            pac += 1
            lis.clear()
    else:pass
print(pac)
