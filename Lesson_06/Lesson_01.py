def f(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = f(int, num)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(f(lambda x: (x, x ** 2,), res))
print(res)


data = '12 33 44 55'

data = list(map(int, data.split()))
print(data)

num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

res2 = list(filter(lambda x: x % 10 ==5, num2))

print(res2)