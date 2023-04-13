# Задача No15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком
# много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9 Output: 1 9

import random

watermelons = int(input('Введите количество арбузов: '))

MAX_WEIGHT = 10
MIN_WEIGHT = 1
weight = 0

min_weight = MAX_WEIGHT
max_weight = MIN_WEIGHT

for i in range(watermelons):
    weight = random.randint(MIN_WEIGHT,MAX_WEIGHT)
    print(weight, end=" ")

    if weight > max_weight:
        max_weight = weight
    if weight < min_weight:
        min_weight = weight
print(f'\nАрбуз для тещи: {min_weight} кг; Арбуз для себя: {max_weight} кг.')