students = []
names = []
if __name__ == '__main__':
    for _ in range(int(input())):
        students.append([])
        name = input()
        score = float(input())
        students[_].append(name)
        students[_].append(score)
    low = students[0][1]
    low2 = None
    for i in range(len(students[1:])):
        if students[i+1][1] < low:
            low2 = low
            low = students[i+1][1]
        elif (low2 is None or low2 > students[i+1][1]) and low != students[i+1][1]:
            low2 = students[i+1][1]
    for i in range(len(students)):
        if students[i][1] == low2:
            names.append(students[i][0])
    names.sort()
    print(*names, sep='\n')