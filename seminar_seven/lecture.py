my_string = '1234567890'
my_string_one = '123wer45678wer90'
my_string = list(my_string)
print(my_string)

for i in range(len(my_string)):
    my_string[i] = int(my_string[i])

print(my_string)

my_string = list(map(int, my_string))
print(my_string)

my_string_one = '123wer45678wer90'
my_string_one = list(my_string_one)
print(my_string_one)


def is_digit(num: str):
    return num.isdigit()


# my_string_one = list(filter(is_digit, my_string_one))
# my_string_one = list(map(int, filter(is_digit, my_string_one)))
# print(my_string_one)

for i, item in enumerate(my_string_one, 5):
    print(i, item)

my_num = '1234567890'
my_let = 'asdfghjklz'
list_1 = list(my_num)
list_2 = list(my_let)
print(list_1)
print(list_2)

# new_list = []
# for i in range(len(list_1)):
#     new_list.append((list_1[i], list_2[i]))
# print(new_list)

new_list = list(zip(list_1, list_2))
print(new_list)

# my_string_one = list(filter(is_digit, my_string_one))
my_string_one = list(filter(lambda x: x.isdigit(), my_string_one))
my_string_one = list(filter(lambda x: x == '1', my_string_one))
print(my_string_one)

# lambda x, y: x + y
