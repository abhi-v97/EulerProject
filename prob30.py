"""

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
# calculated by hand, upper bound seems to be 300000

def fifth_power_sum(n):
    return sum(int(i)**5 for i in str(n))

def compute():
    total = sum(i for i in range(2,300000) if i == fifth_power_sum(i))
    return str(total)

if __name__ == "__main__":
	print(compute())