"""

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import functools

def compute():
    ans = 1
    for i in range(1, 1000000):
        seq = collatz_chain_length(i)
        if  seq > ans:
            ans = seq
            start_num = i
    return str(ans), str(start_num)

#cache stores function arguments and results, reusing them recurisvely as needed
#drastically reduces time taken, as it can easily look up cached result while counting
#chain length
@functools.cache
def collatz_chain_length(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        y = x // 2
    else:
        y = x * 3 + 1
    #print(y)
    
    #loop to start of function. The +1 adds one to the return value per loop, so a value with
    #collatz length of 4 essentially returns 1 + 1 + 1 + 1.
    return collatz_chain_length(y) + 1

if __name__ == "__main__":
    print("Starting number =", compute()[1], ",Sequence Length =", compute()[0])

