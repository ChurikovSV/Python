'''Задача №19. Общее обсуждение
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально.'''


def move(list, pivot):
    
    pivot = pivot % len(list)
    
    left_list = list[:-pivot]
    right_list = list[-pivot:]
    moved_list = right_list + left_list
    return moved_list


def move1(list, pivot):
    pivot = pivot % len(list)
    
    for i in range(pivot):
        list.insert(0, list.pop())
        
    

input_list = [1, 2, 3, 4, 5]
k = 4
    
print(move(input_list, k))

print(move1(input_list, k))