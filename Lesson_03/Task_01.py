'''Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.'''

n = int(input("Введите число "))

result = 1
while n > 0:
    result = result * n
    n -= 1
    
print(result)