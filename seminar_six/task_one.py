# Задача No39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12
# (каждое число вводится с новой строки)
import random


# Первый вариант
def input_numbers(minn, maxx, size):
    input_number = [random.randint(minn, maxx) for _ in range(size)]
    return input_number


first_list = input_numbers(1, 10, 10)
second_list = input_numbers(1, 5, 5)
print(first_list)
print(second_list)


def new_list(first_list, second_list):
    new_list = list()
    for item in first_list:
        if item not in second_list:
            new_list.append(item)
    return new_list


print(new_list(first_list, second_list))

# Второй вариант

list_1 = [random.randint(1, 20) for _ in range(20)]
list_2 = [random.randint(1, 10) for _ in range(10)]
print(list_1)
print(list_2)

unique_list = [i for i in list_1 if i not in list_2]
print(unique_list)
