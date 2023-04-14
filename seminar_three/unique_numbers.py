# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в
# нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
import random

# Первый вариант

size = int(input('Введите размер списка: '))
my_list = [random.randint(-5, 5) for _ in range(size)]
print(my_list)

my_set = set(my_list)
print(my_set)

print(f'Количество уникальных значений: {len(my_set)}')


# Второй вариант

list_num = list(input('Введите список чисел: '))

unique_list = []
for item in list_num:
    if not item in unique_list:
        unique_list.append(item)

print(list_num)
print(unique_list)

