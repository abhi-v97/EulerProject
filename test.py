# brute force
x = 0
y = 0

for i in range(1, 101):
    x += i * i
    y += i

print(y, x, (y*y) - x)