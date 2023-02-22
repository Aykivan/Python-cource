# Чтение:
# with open('test.txt', 'r', encoding='utf-8') as file:
#     # text = file.read().splitlines()
#     # print(text)


    # while True:
    #     line = file.readline()
    #     if not line:
    #         break
    #     print(line.strip())
# данная запись позволяет выводить все строки через бесконечный цикл, пока строка не равна пустоте

# file.read().splitlines() - записывает каждую строку в отдельный элемент и выводит в виде списка строк
# file.readlines() - добавляет на конце \n 
# print(line.strip()) - выводит строки без всяких пробелов энтеров и тд

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Запись:

# with open('test.txt', 'w', encoding='utf-8') as file:
#     some_list = ['привет', 'пока']
#     for word in some_list:
#         file.write(word + '\n')

# Файл будет перезаписан при использовании 'w', если хотим его дополнить используем 'a'

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Необходимо создать файл, ввести букву, количество которой нужно посчитать

# find_el = input('Введите букву поиска: ')

# with open('test.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     count = 0
#     print(text)
#     for el in text:
#         if el == find_el:
#             count += 1
#     print(count)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# import random

# n = int(input('Введите количество элементов: '))

# list_n = [random.randint(-n, n) for _ in range(n)]
# print(list_n)

# with open('test.txt', 'w', encoding='utf-8') as file:
#     for el in range(n):
#         file.write(str(random.randint(1, n - 1)) + '\n')
#     print(file)

# with open('test.txt', 'r', encoding='utf-8') as file:
#     mult = 1
#     for ind in file.read().splitlines():
#         mult *= list_n[int(ind)]
# print(mult)




# from random import randint
# n = int(input('Введите кол-во элементов в списке: '))
# some_list = [randint(-n, n) for _ in range(n)]
# print(some_list)
# with open('les8test.txt', 'w', encoding='utf-8') as file:
#     for _ in range(randint(1, n)):
#         file.write(str(randint(0, n - 1)) + '\n')

# with open('les8test.txt', 'r', encoding='utf-8') as file:
#     mult = 1
#     for ind in file.read().splitlines():
#         mult *= some_list[int(ind)]
# print(mult)
