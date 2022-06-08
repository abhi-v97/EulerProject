#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.

import prob7

def sum_primes(n):
    s = sum(prob7.sieveOfEratosthenes(n))
    return s

if __name__ == "__main__":
    x = 2000000
    print(str(sum_primes(x)))
