# Задача No37. Решение в группах
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать
# циклы (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3


n = 'qwerty'
print(n)


def revers(n):
    if len(n) == 1:
        return n
    return n[-1] + revers(n[:-1])


print(revers(n))


def rev_one(number):
    if number == 1:
        return '1'
    return f'{number} {rev_one(number - 1)}'


print(rev_one(5))
