"""The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

# brute force
x = 0
y = 0

for i in range(1, 101):
    x += i * i
    y += i

print((y*y) - x)

#done using sum formulas

#sum of natural numbers: sum = n(n+1)/2
#sum of squares: sum_sq = n(n+1)(2n+1)/6
#not that much faster, surprisingly

n = 100
sum = n * (n + 1) * 0.5
sum_sq = n * (n + 1) * (2 * n + 1) / 6
ans = sum * sum - sum_sq

print(int(ans))
