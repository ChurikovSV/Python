'''Задача №17. Общее обсуждение
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]'''

input_list = [1, 1, 2, 0, -1, 3, 4, 4]

def get_set(list):

    return len(set(list))

print(get_set(input_list))