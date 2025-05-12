# 1351. Count Negative Numbers in a Sorted Matrix
# Difficulty: Easy

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
 

# Follow up: Could you find an O(n + m) solution?

# Solution:

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        C = len(grid[0])
        res = 0

        for row in grid:
            l, r = 0, C - 1
            while l <= r:
                m = (l + r) // 2
                if row[m] >= 0:
                    l = m + 1
                else:
                    r = m -1
            res += (C - l)
        return res


# Create an instance of the Solution class
solution = Solution()

# Test case 1

grid1 = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
result1 = solution.countNegatives(grid1)
print(result1)  # Output: 8

# Test case 2

grid2 = [[3, 2], [1, 0]]
result2 = solution.countNegatives(grid2)
print(result2)  # Output: 0

# Test case 3

grid3 = [[-1]]
result3 = solution.countNegatives(grid3)
print(result3)  # Output: 1