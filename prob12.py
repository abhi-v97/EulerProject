"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import itertools
from math import sqrt, floor


# Returns the number of integers in the range [1, n] that divide n.
def num_divisors(n):
    end = floor(sqrt(n))
    divs = []
    for i in range(1, end + 1):
        if n % i == 0:
            divs.append(i)
    if end**2 == n:
        divs.pop()
    return 2*len(divs)


def compute():
    triangle = 0
    for i in itertools.count(1):
        # This is the ith triangle number, i.e. num = 1 + 2 + ... + i =
        # = i*(i+1)/2
        triangle += i
        if num_divisors(triangle) > 500:
            return str(triangle)
            
if __name__ == "__main__":
    print(compute())