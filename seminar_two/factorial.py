# Задача No9. Решение в группах
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

my_limit = int(input('Введите предел факториала: '))

factorial = 1
count = 1

while count <= my_limit:
    factorial *= count
    count += 1

print(factorial)