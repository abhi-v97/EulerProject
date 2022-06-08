#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10,001st prime number?

"""
Sieve of Eratosthenes 
Ancient, efficient algorithm to find prime numbers to any given limit


Steps
-Write all numbers down
-Start at 2, as 1 is not prime
-Circle 2, cross all multiples of 2, since each of those numbers has 2 as a factor, therefore not prime
-Next, circle 3, cross every multiple of 3.
-Then 5, then 7, then 11. Stop when all numbers are crossed or circled.
"""

def sieveOfEratosthenes(num):

    #create a blank list that says True for each i in num
    prime = [True for i in range(num+1)]

    x = 2
    prime_num = []

    while(x * x <= num):
        
        #only do this if number is a prime
        #if not prime, move onto next number
        if (prime[x] == True):

            #change all multiples of x
            for i in range(x*x, num+1, x):
                prime[i] = False
        
        x += 1

    for i in range(2, num+1):
        if prime[i]:
            prime_num.append(i)

    return prime_num

if __name__ == "__main__":
    prime_num = sieveOfEratosthenes(1000000)
    print(prime_num[10000])
