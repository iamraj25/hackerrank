# n = int(input())
# word_list = []
# unique_list = []
# for i in range(n):
#     word_list.append(input())
# x = set(word_list)
# print(len(x))
# for i in word_list:
#     if i not in unique_list:
#         unique_list.append(i)
#         print(word_list.count(i), end=" ")

from collections import OrderedDict

words = OrderedDict()

for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1

print(len(words))
print(*words.values())