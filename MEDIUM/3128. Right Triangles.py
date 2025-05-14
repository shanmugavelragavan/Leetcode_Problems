# 3128. Right Triangles
# Difficulty: Medium

# You are given a 2D boolean matrix grid.

# A collection of 3 elements of grid is a right triangle if one of its elements is in the same row with another element and in the same column with the third element. The 3 elements may not be next to each other.

# Return an integer that is the number of right triangles that can be made with 3 elements of grid such that all of them have a value of 1.

 

# Example 1:

# 0	1	0
# 0	1	1
# 0	1	0
# 0	1	0
# 0	1	1
# 0	1	0
# 0	1	0
# 0	1	1
# 0	1	0
# Input: grid = [[0,1,0],[0,1,1],[0,1,0]]

# Output: 2

# Explanation:

# There are two right triangles with elements of the value 1. Notice that the blue ones do not form a right triangle because the 3 elements are in the same column.

# Example 2:

# 1	0	0	0
# 0	1	0	1
# 1	0	0	0
# Input: grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]

# Output: 0

# Explanation:

# There are no right triangles with elements of the value 1.  Notice that the blue ones do not form a right triangle.

# Example 3:

# 1	0	1
# 1	0	0
# 1	0	0
# 1	0	1
# 1	0	0
# 1	0	0
# Input: grid = [[1,0,1],[1,0,0],[1,0,0]]

# Output: 2

# Explanation:

# There are two right triangles with elements of the value 1.

 

# Constraints:

# 1 <= grid.length <= 1000
# 1 <= grid[i].length <= 1000
# 0 <= grid[i][j] <= 1

# Solution:

from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        row, col = [0] * R, [0] * C
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    row[r] += 1
                    col[c] += 1
        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    res +=  (row[r] - 1) * (col[c] - 1)
        return res
    

# Define the grid input
grid1 = [[0, 1, 0],
         [0, 1, 1],
         [0, 1, 0]]

grid2 = [[1, 0, 0, 0],
         [0, 1, 0, 1],
         [1, 0, 0, 0]]

grid3 = [[1, 0, 1],
         [1, 0, 0],
         [1, 0, 0]]

# Create an instance of Solution
solution = Solution()

# Call the numberOfRightTriangles method for each grid
result1 = solution.numberOfRightTriangles(grid1)
result2 = solution.numberOfRightTriangles(grid2)
result3 = solution.numberOfRightTriangles(grid3)

# Output the result for each grid
print(f"Result for grid1: {result1}")
print(f"Result for grid2: {result2}")
print(f"Result for grid3: {result3}")