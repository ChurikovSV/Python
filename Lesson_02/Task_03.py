num = 987
result = 0
print(num % 10)

while num > 0:
    i = num % 10
    result = result + i
    num = num // 10
    
print(result)

