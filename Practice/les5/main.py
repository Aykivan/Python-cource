# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2) 

# n = int(input('Введите число N: '))
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# list_fib = []
# for i in range(n):
#     list_fib.append(fib(i))
    
# print(*list_fib)
# print(fib(n))

# ---------------------------------------------------------------------------------------------------------------------------------------

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# import time

# magizine = [int(input('Введите оценку: ')) for _ in range(int(input('Введите количество оценок: ')))]   
# list comprehension

# Нахождение с помощью встроенной функции
# start = time.perf_counter()
# minn = min(magazin)
# maxx = max(magazine)
# end = time.perf_counter()
# print(end - start)
# # Нахождение с помощью одного цикла
# minn = magazine[0]
# maxx = magazine[0]
# for el in magazine:
#     if maxx < el:
#         maxx = el
#     if minn > el:
#         minn = el

# n = int(input('введите количество оценок: '))
# list_1 = []

# min_mark = 5
# max_mark = 0
# list_1 = [int(input(f'Введите оценку: ')) for i in range(n)]
# for i in list_1:
#     if i < min_mark:
#         min_mark = i
#     if i > max_mark:
#         max_mark = i
# print(min_mark, max_mark)
# print(list_1)

# for i in range(len(list_1)):
#     if list_1[i] == min_mark:
#         list_1[i] = max_mark
# print(list_1)

# ---------------------------------------------------------------------------------------------------------------------------------------

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

def check_num(n):
    if n == 2:
        return True
    else: 
        for i in range(2, n// 2 + 1):
            if n % i == 0:
                return False
            else:
                return True

n = int(input('Введите проверяемое число: '))
prov = check_num(n)
if prov == True:
    print(f'Число {n} является простым')
else:
    print(f'Число {n} не является простым')

