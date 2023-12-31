'''Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
'''

n = 385916
count = 0

res1 = 0
res2 = 0

while count < 3:
    count += 1
    i = n % 10
    res1 = res1 + i
    n = n // 10
else:
     while n > 0:
        j = n % 10
        res2 = res2 + j
        n = n // 10   
        
if res1 == res2:
    print("YES")
else:
    print("NO")

