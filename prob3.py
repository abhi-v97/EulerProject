n = 600851475143 

def largest_prime_factor(num):
    i = 2
    while i * i <= num: #looking for factors so stop when i^2 is greater than n
        if num % i:     #if there is a modulus, move onto next integer
            i+=1
        else:
            num //= i  
            #once you find first factor, divide number by prime and use result for the next loop
            #no i+=1 as there may be repeat prime numbers
            #print(num, i)
    return num

def prime_factors(num): #modified the method to return a list of factors instead
    i = 2
    factors = []
    while i * i <= num: #looking for factors so stop when i^2 is greater than n
        if num % i:     #if there is a modulus, move onto next integer
            i+=1
        else:
            num //= i  
            factors.append(i)
    if n > 1:
        factors.append(num) #add the last prime, left out by the previous loop

    return factors

if __name__ == "__main__":
    print(largest_prime_factor(n))
    print(prime_factors(n))   