'''Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
Найдите количество и выведите его.'''

list_1 = [1, 2, 3, 3, 4, 5]
k = 3


element = 0

for i in list_1:
    if k == i:
        element += 1

print(element)