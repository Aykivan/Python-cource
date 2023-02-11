# Задача №25.
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# string = 'a a a b c a a d c d d'
# print(string)
# my_list = string.split() 
# my_dict = {}
# new_list = []

# for letter in my_list:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
#     if my_dict.get(letter) > 1:
#         new_list.append(letter + '_' + str(my_dict.get(letter)))
#     else:
#         new_list.append(letter)
# print(' '.join(new_list))

# letter - значение ключа в словаре my_dict 
# .get(letter, 0) + 1 - функция get запрашивает значение из словаря по ключу letter, если такого ключа в словаря нет, 
# она создает его и присваивает ему значение после запятой, то есть 0, если же ключ такой в словаре есть, get переписывает его 
# на его значение + 1, таким образом мы получаем своего рода словарь счетчик
# if my_dict.get(letter) > 1: - так как нам не нужно указывать первые элементы, мы задаем условие, что если значения по проверяемому 
# ключу больше 1, то мы добавляем значение в новый список с приставкой которую насчитали от 2 до N
# .join - позволяет нам прописать все значения списка через элемент в ковычках

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# my_string = 'she sells sea shells on   sells  the sea shore The  sell'

# my_string = input('Введите текст: ')
# my_set = set(my_string.split())
# # - преобразовали строку во множество разделенное пробелами
# print(my_string)
# print(my_set)
# # for i i
# print(f' в намеш тексте уникальных слов - {len(my_set)}')
# - вывели количество эдементов множества

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Дана последовательность чисел. Получить список уникальных элементовзаданной последовательности
# [1, 2, 4, 32, 12, 11, 5, 6, 77, 10, 22, 1, 2, 4, 32]

# nubs = [1, 2, 3, 5, 1, 5, 3, 10]
# print(nubs)
# my_dict = {}
# un_list = []

# for n in nubs:
#     my_dict[n] = my_dict.get(n, 0) + 1
# print(my_dict)

# for i in my_dict:
#     if my_dict[i] == 1:
#         un_list.append(i)
# print(un_list)

#  Правильное решение

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# new_list = []
# for item in my_list:
#     if my_list.count(item) == 1:
#         new_list.append(item)
# print(new_list)
#  print([letter for latter in my_list if my_list(latter).count == 1])
#  1 letter - элемент который мы добавляем
#  for latter in my_list - пробегаемся по элементам в массиве май лист 
#  if my_list(latter).count == 1 - если условие выполнено добавляем 1 letter
# .count - функция которая считает количество повторений эл-та в списке

# my_list = set(nubs.split())
# print(*my_list)