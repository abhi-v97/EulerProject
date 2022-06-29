
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
# figure out the diagonals of an ulam spiral
# top right will always be n^2, where n is the length/width of spiral
# Since we know what top right is, we can deduce top left, as it will always be n^2 - (n - 1)
# Since we know top left, we can work out bottom left which is top left minus n - 1,
# so n^2 - 2(n - 1)
# and from that logic bottom right is n^2 - 3(n - 1)
# the spiral consists of multiple circles. Add the diagonals at each stage and we get the sum of
# the whole spiral
# n always increases in steps of 2

def compute():
    size = 1001
    total = 1
    total += sum(4 * n ** 2 - 6 * (n - 1) for n in range(3, size + 1, 2))
    return str(total)


if __name__ == "__main__":
    print(compute())
