"""https://projecteuler.net/problem=27"""

from prob7 import sieveOfEratosthenes
from functools import cache

@cache
def is_prime(n):
    prime = True
    if n <= 1:
        return False
    elif n > 1:
        for i in range (2, n):
            if n % i == 0:
                prime = False
                break
    
    return prime

#print(is_prime(2))

#n^2 an + b should equal prime
#for any a, n = 0 returns b, therefore b has to be prime
#the question requires b <= 1000, so start by finding all primes to 1000


prime_1000 = sieveOfEratosthenes(1000)

def compute():
    longest = 0
    long_a = 0
    long_b = 0
    for a in range(-1000, 1000): 
        for b in prime_1000: #no negative primes, so b has to be positive
            n = 0
            rhs = n ** 2 + a * n + b # rhs = right hand side

            while is_prime(rhs):
                rhs = n ** 2 + a * n + b
                n += 1
        
            if n > longest:
                longest = n
                long_a = a
                long_b = b

    return long_a * long_b


if __name__ == "__main__":
	print(compute())