"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
#40 steps needed to reach the corner, 20 steps in eiher x or  y with no backtracking.
#Therefore, we simply calculate 40 choose 20.

#This works for their example, where it would be 4 choose 2 which equals 6.

from math import factorial 

ans = factorial(40) / (factorial(20) * factorial(20))
print(ans)