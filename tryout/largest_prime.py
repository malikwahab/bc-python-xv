def largest_prime_number(n):
   i = 2
   while i * i < n:
       while n%i == 0:
           n = n / i
       i = i + 1
   else:
       if i**2 == n:
           return i
   return n

print(largest_prime_number(600851475143))
