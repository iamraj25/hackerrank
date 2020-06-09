# def false(f):
#     if f == 0:
#         print(False)
#
#
# if __name__ == '__main__':
#     s = input()
#     for i in s:
#         if i.isalnum():
#             print("True")
#             break
#         elif s.index(i) == len(s) - 1:
#             f = 0
#             false(f)
#             break
#     for i in s:
#         if i.isalpha():
#             print("True")
#             break
#         elif s.index(i) == len(s) - 1:
#             f = 0
#             false(f)
#             break
#     for i in s:
#         if i.isdigit():
#             print("True")
#             break
#         elif s.index(i) == len(s) - 1:
#             f = 0
#             false(f)
#             break
#     for i in s:
#         if i.islower():
#             print("True")
#             break
#         elif s.index(i) == len(s) - 1:
#             f = 0
#             false(f)
#             break
#     for i in s:
#         if i.isupper():
#             print("True")
#             break
#         elif s.index(i) == len(s) - 1:
#             f = 0
#             false(f)
#             break


if __name__ == '__main__':
    s = input()
    for i in s:
        if i.isalnum():
            print("True")
            break
    else:
        print(False)
    for i in s:
        if i.isalpha():
            print("True")
            break
    else:
        print(False)
    for i in s:
        if i.isdigit():
            print("True")
            break
    else:
        print(False)
    for i in s:
        if i.islower():
            print("True")
            break
    else:
        print(False)
    for i in s:
        if i.isupper():
            print("True")
            break
    else:
        print(False)