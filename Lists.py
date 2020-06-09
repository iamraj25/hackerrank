if __name__ == '__main__':
    N = int(input())
    n = []
    list = []
    for i in range(N):
        n.append(input().split())
    for i in range(N):
        if n[i][0] == 'insert':
            list.insert(int(n[i][1]), int(n[i][2]))
        elif n[i][0] == 'print':
            print(list)
        elif n[i][0] == 'remove':
            list.remove(int(n[i][1]))
        elif n[i][0] == 'append':
            list.append(int(n[i][1]))
        elif n[i][0] == 'sort':
            list = sorted(list)
        elif n[i][0] == 'pop':
            list.pop()
        elif n[i][0] == 'reverse':
            list.reverse()
        else:
            pass