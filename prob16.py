"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

def compute():
    n = 2**1000
    ans = sum(int(i) for i in str(n))

    return str(ans)

if __name__ == "__main__":
    print(compute())