# Задача No19. Решение в группах
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения списка или список задан изначально.
import random

# Первый вариант

size = int(input('Введите размер списка: '))
my_list = [random.randint(0, 10) for _ in range(size)]
print(my_list)

shift_value = int(input('Введите количество сдвигов: '))
for i in range(shift_value):
    my_list.insert(0, my_list.pop())

print(my_list)

# Второй вариант

my_list = list(input('Введите числа: '))
value_shift = int(input('Введите количество сдвигов: '))

new_list = my_list[-value_shift:] + my_list[:-value_shift]
print(new_list)


