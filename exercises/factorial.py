from functools import reduce

def reduce_factorial(n):
    if n < 1:
        return False
    return reduce(lambda x,y:x*y , range(1, n+1))

def recusion_factorial(n):
    if n < 1:
        return False
    elif n == 1:
        return n
    else:
        return n*recusion_factorial(n-1)


print(reduce_factorial(10))
print(recusion_factorial(10))
