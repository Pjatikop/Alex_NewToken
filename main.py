# name = "Алексей"
# print("Hello", name)
# age = 20
# print(age)
# print(id(age))

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)

# print(56565656565665)

# a, b, c = 5, 7, 3
# print("Сумма = ", a + b + c)
# print("Произведение = ", a * b * c)
# print("Среднее арифметическое = ", (a + b + c) // 3)


# num = int(input("Введите число: "))
# a = int(input("Введите степень: "))
# print("Число ", num, " в степени ", a, " равно ", (num ** a), sep="")


# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1

# i = int(input("Start: "))
# j = int(input("End: "))
# sum1 = 0
# while i != j:
#     if i % 2 != 0:
#         sum1 += i
#     i += 1
# print(sum1)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# sum = 0
# for i in a:
#     if i < 0:
#         sum += i
# print(sum)

# a = int(input("Введите количество строк: "))
# b = int(input("Введите количество столбцов: "))
#
# for i in range(a):
#     for j in range(b):
#         if i == 0 or j == 0 or i == a - 1 or j == b - 1:
#             print("*", end="")
#
#         else:
#             print(" ", end="")
#     print()
# s = []
# n = int(input("Введите количество элементов: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 != 0:
#         print(str(x) + " не делится на 3 без остатка")
#     else:
#         s.append(x)
# print(s)

# a = [1, 2, 3]
# b = [11, 12, 13]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)
# import random
# n = int(input("Размер списка: "))
# s = []
# while len(s) < n:
#     num = random.randrange(n)
#     if num not in s:
#         s.append(num)
# print(s)

# from random import randint
#
# w, h = 3, 4
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
# print(matrix)
# [print(('\t'.join([str(x) for x in row])), end="\n") for row in matrix]
# [[print(matrix[j][i], end="\t") for i in range(len(matrix[j]))] for j in range(len(matrix))]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# s = list(input("->"))
# s = [int(s[i]) for i in range(len(s))]
#
# print(s)

# Задача: вывести ромб из звездочек

# a = 5
#
# for i in range(a):
#     for j in range(a):
#         if i == a // 2 or j == a // 2:
#             print("*", end="")
#         elif (i + j == 2 and i != 0 and j != 0) or (i + j == 4 and i != 0 and j != 0) or (i + j == 6 and i != 0 and j != 0):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# a = int(input("Введите число: "))
# f = 1
# for i in range(1, a + 1):
#     f *= i
#
# print("Факториал:", f)

# def to_set(a):
#     return set(a), len(set(a))
#
# b = "я обычная строка"
# print(to_set(b))

# a = "Python"
# b = "Programming language"
# c = set(a) - set(b)
# for i in c:
#     print(i, end=" ")

# a = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# s = 1
# for i in a:
#     s *= a[i]
# print(s)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {}
# z.update(x)
# z.update(y)
# print(z)

# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4738, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3908, "S": 3645, "E": 8821, "W": 2451}
# }

# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ": ", sales[x][y], sep="")
#
# name = input("Имя: ")
# reg = input("Регион: ")
# print(sales[name][reg])

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = result.get(num, 0) + 1
#
# print(result)

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]

# result = {}
#
# for i in pets:
#     if result or (i[1:] not in result):
#         result[i[1:]] = [i[0]]
#     elif i[1:] in result:
#         result[i[1:]].append(i[0])
#
# print(result)

# list1 = [i.strip('.,!?:;-').lower() for i in input("Введите текст: ").split()]
# dct2 = {i: list1.count(i) for i in set(list1) if i}
# print(min(i for i in dct2 if dct2[i] == min(dct2.values())))

# words = input().split()
#
# res = {}
# for i in words:
#     res[i] = res.get(i, 0) + 1
#     if res[i] != 1:
#         print(f'{i}_{res[i] - 1}', end=" ")
#     else:
#         print(i, end=" ")

# d = {}
# for c in input().lower():
#     d[c] = d.get(c, 0) + 1
#
# for c in input().lower():
#     d[c] = d.get(c, 0) - 1
#
# print([set(d.values()) == {0}])
# print(('NO', 'YES')[False])
# def fun(*a):
#     return [i for i in a if i < sum(a) / len(a)]
#
#
# print(fun(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(fun(3, 6, 1, 9, 5))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# print((lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c)(9, 8, 5))

# a = (lambda x, y: x + y)
# print(a(1, 2))
# res ={}
# val = {'a': 1, 'b': 2}
# for k, v in val.items():
#     res.setdefault(k, set()).add(v)
# print(res)


# print([i for i in range(5)])

# print("ASD")
# a = 10
# print(a)

# from random import shuffle
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# matrix1 = [j for i in range(len(matrix)) for j in matrix[i]]
# shuffle(matrix1)
# matrix = [[matrix1.pop(0) for _ in range(4)] for _ in range(4)]
# print(matrix)

# from random import randint
# n = 7
# res = set()
# while len(res) < 100:
#     num = [str(randint(0, 9)) for _ in range(n)]
#     if num[0] != '0':
#         res.add(''.join(num))
# print(*res, sep='\n')

# from random import shuffle
#
# word = list(input())
# shuffle(word)
# print(*word, sep='')

# from random import randint
#
# def print_matrix(mat, n, width=3):
#     for r in range(n):
#         for c in range(n):
#             print(str(mat[r][c]).ljust(width), end=' ')
#         print()
#
#
# l = 5
# p = set()
# while len(p) < l ** 2:
#     p.add(randint(1, 75))
# lst = list(p)
# matrix = [[lst.pop(0) for _ in range(l)] for _ in range(l)]
# matrix[l // 2][l //2] = 0
# print_matrix(matrix, l)
# ------------------------------------------------------------------------------------------------

# from random import shuffle
#
# n = int(input())
# inp1 = [input() for _ in range(n)]
# inp2 = inp1.copy()
# k = 0
# while k != n:
#     k = 0
#     shuffle(inp2)
#     for i in range(len(inp1)):
#         if inp1[i] != inp2[i]:
#             k += 1
#
# print(*[inp1[i] + " - " + inp2[i] for i in range(len(inp1))], sep="\n")

# ------------------------------------------------------------------------------------------------------------

# import turtle
#
# def star(side):
#     turtle.showturtle()
#     turtle.right(60)
#     for j in range(10):
#         for i in range(4):
#             turtle.forward(side)
#             turtle.left(60 + (i % 2) * 60)
#         turtle.left(35)
#
#
# star(100)

# s = input("Введите дату в формате: ")


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# count = 0
# for i in names:
#     if isinstance(i, list):
#         for j in i:
#             if isinstance(j, list):
#                 for k in j:
#                     count += 1
#             else:
#                 count += 1
#     else:
#         count += 1

# print(count)
from random import randint
import time
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
# lst = [randint(1, 99) for i in range(10000)]
# start = time.monotonic()
# bubble(lst)
# res = time.monotonic() - start
# print(round(res, 3), 'sec')


# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#
#     left = merge_sort(a[:n // 2])
#     right = merge_sort(a[n // 2: n])
#
#     i = j = 0
#     res = []
#
#     while i < len(left) or j < len(right):
#         if not i < len(left):
#             res.append(right[j])
#             j += 1
#         elif not j < len(right):
#             res.append(left[i])
#             i += 1
#         elif left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#         return res
#
# array = [randint(1, 99) for i in range(10000)]
#
# start = time.monotonic()
# array = merge_sort(array)
# res = time.monotonic() - start
# print(round(res, 3), 'sec')

