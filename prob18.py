"""
https://projecteuler.net/problem=18



By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)


"""
grid = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]
total = []

pos = 0
count = 0
path = 0
current = 0
i = 0

#print(grid[14][2])

#bottom's up approach
#range(start = 14, stop = 0, steps = -1)
#start at len(grid)-1 = 14 which is the last row
#stop in range is exclusive, so -1 to stop at 0
#in steps of -1
def compute(grid):
        for x in range(len(grid)-1,-1,-1):        
                for y in range(0,x):
                        grid[x-1][y]+=max(grid[x][y],grid[x][y+1])

        return grid[0][0]


def path_to_bottom():
        
    res = grid
    result_arr = res[0]
    
    for row in res[1:]:
        
        new_res = []
        for x,value in enumerate(row):
                #print(x, value)
                if x==0:
                        # 1st element of row
                        new_res += [value+result_arr[0]]
                        
                elif x==len(row)-1:
                        # last element of row
                        new_res += [value + result_arr[-1]]
                        
                else:
                        # mid-elements of row
                        new_res += [value+max(result_arr[x],result_arr[x-1])]
        
        
        result_arr = new_res
        

        
if __name__ == "__main__":
    #print(compute())
    path_to_bottom()
