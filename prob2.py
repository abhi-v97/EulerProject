ans = 0
x = 1  #current Fibonacci number being processed
y = 2  #next Fibonacci number in the sequence

while x <= 4000000:
    if x % 2 == 0:
        ans += x
    x, y = y, x + y

if __name__ == "__main__":
	print(ans)