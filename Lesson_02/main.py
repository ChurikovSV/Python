'''
i = int(input("Введите число "))
print(f"квадрат числа {i ** 2}")
print(f"целочисленное деление на 3 этого числа {i // 3}")
print(f"остаток от деления числа на 3 {i % 3}")

if i > 0:
    print("больше нуля")
elif i == 0:
    print("Вы ввели ноль")
else:
    print("Отрицательное число")
    
'''

'''
Машина едет н км какое расстояние оно пройдет м км
'''

n = int(input("введите скорость "))
m = int(input("введите расстояние "))
c = m//n + 1 % (m%n +1)

print(c)

'''
В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
'''

a = int(input("кол-во уч. в первом классе "))
b = int(input("кол-во уч. в втором классе "))
c = int(input("кол-во уч. в третьем классе "))

result1 = a // 2 + a % 2
result2 = b // 2 + b % 2
result3 = c // 2 + c % 2

print(a // 2)
print(a % 2)

print(result1)
print(result2)
print(result3)

print(result1 + result2 + result3)


'''
Вещественное число
'''

n = abs(float(input("Введите число ")))

sum = 0
while n % (10) > 0:
    n = n * 10
    
while n > 0:
    sum = sum + n % 10
    n = n // 10
print(sum)
    