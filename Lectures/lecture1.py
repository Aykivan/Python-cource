# Способы вывода данных

# a = 5
# b = 1.34
# c = 'hello'

# print(a,' - ',b,' - ',c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))

# Ввод данных 

# print('Введите первое число: ')
# a = int(input())
# print(a)
# b = int(input('Введите второе число: '))
# print(a, ' + ', b, ' = ', a + b)

# Округление чисел

# a = 3.1212
# b = 2.2111323
# print(round(a*b, 3))

# Сокращенное присваивание 

# username = input('Введите ваше имя: ')
# if username == 'Иван':
#     print('Ура, это ИВАН!')
# elif username == 'Ваня':
#     print('Ура, это Ваня!')
# elif username == 'Настя':
#     print('Салам, Настя!')
# else:
#     print('Привет, ', username, '!')


# for i in 'qwerty':
#     print(i)

# a = 'qwerty'
# print(a[3])


for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)