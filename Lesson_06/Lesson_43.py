'''Семинар 6. Повторение списков
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.'''

lst1 = [1, 2, 3, 2, 3]

print(sum(lst1.count(i)//2 for i in set(lst1)))