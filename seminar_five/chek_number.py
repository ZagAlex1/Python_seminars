# Задача No35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes

# Первый вариант

# number = int(input('Введите число: '))
#
#
# def is_simple(num: int) -> bool:
#     if num in [1, 2]:
#         return True
#     elif not num % 2:
#         return False
#     else:
#         for i in range(3, num // 2 + 1, 2):
#             if num % i == 0:
#                 return False
#     return True
#
#
# print(f'Число {number} ' + ('простое' if is_simple(number) else 'комплексное'))

# Второй вариант

# check_number = int(input('Введите число для проверки: '))
#
# count = 0
#
# for item in range(1, check_number + 1):
#     if check_number % item == 0:
#         count += 1
# print(f'Число {check_number} ' + ('простое' if count == 2 else 'комплексное'))

# Третий вариант


check_number = int(input('Введите число для проверки: '))

count = 0

for item in range(2, check_number // 2 + 1):
    if check_number % item == 0:
        count += 1
print(f'Число {check_number} ' + ('простое' if count == 0 else 'комплексное'))
