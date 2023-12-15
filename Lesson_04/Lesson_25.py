'''Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2'''

def count_symbs(symbs):
    new_symbs = []
    for i in range(len(symbs)):
        n = symbs[:i + 1].count(symbs[i]) - 1
        if n == 0:
            new_symbs.append(symbs[i])
        else:
            new_symbs.append(f"{symbs[i]}_{n}")
        
    return new_symbs
    
string = "a a a b c a a d c d d"
list_1 = string.split()
new_list = count_symbs(list_1)

print(new_list)


