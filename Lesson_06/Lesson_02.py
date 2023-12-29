from random import randint

def list(lower, upper, count):
    res = []
    
    for i in range(count):
        res.append(randint(lower, upper))    
    return res

print(list(-5, 10, 5))
print([randint(-5, 10) for _ in range (5) ])

sp = [i for i in range(10)]
print(sp)

print( [i ** 2 for i in sp] )
print( [i ** 2 for i in sp if i % 2] )
print( [i ** 2 if i % 2 else 0 for i in sp] )
print( sum([i ** 2 if i % 2 else 0 for i in sp]) )

print( {i: chr(i) for i in range (5)} )
