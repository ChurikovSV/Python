'''Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.'''

n = 16
i = 0

while 2 ** i <= n:
    print(2 ** i)
    i += 1