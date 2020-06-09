def percent_return(query_name):
    average = 0.00
    for i in range(3):
        average += student_marks[query_name][i]
    average = average/3
    return average


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # print(student_marks[query_name])
    avg_per = percent_return(query_name)
    print("{:.2f}".format(avg_per))
