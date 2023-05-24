# Задача No51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True,
# если это так. Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.
# Ввод:                                     Вывод:
# values = [0, 2, 10, 6]                    same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
import random


def same_by(characteristic, objects):
    my_set = set(map(characteristic, objects))
    print(my_set)
    return len(my_set) < 2


my_list = [random.randint(2, 6) for i in range(4)]
print(my_list)

print(same_by(lambda x: x % 2, my_list))
