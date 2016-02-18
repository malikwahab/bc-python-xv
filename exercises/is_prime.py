def is_prime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True
    # all other even numbers are not primes
    # Binary of all even number ends with 0 so even & 0b1 always equal 0
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

print(is_prime(3))
print(is_prime(13))
print(is_prime(12))
print(is_prime(121))
