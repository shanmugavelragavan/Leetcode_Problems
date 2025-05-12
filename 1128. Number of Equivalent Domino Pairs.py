# 1128. Number of Equivalent Domino Pairs
# Difficulty: Easy

# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

# Example 1:

# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# Example 2:

# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3
 

# Constraints:

# 1 <= dominoes.length <= 4 * 104
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9

from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        for domino in dominoes:
            domino.sort()
            domino = tuple(domino)
            d[domino] = d.get(domino, 0) + 1
        res = 0
        for k, v in d.items():
            res += v * (v - 1) // 2
        return res

# Example function call
solution = Solution()

# Example 1
dominoes1 = [[1, 2], [2, 1], [3, 4], [5, 6]]
result1 = solution.numEquivDominoPairs(dominoes1)
print(result1)  # Output: 1

# Example 2
dominoes2 = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
result2 = solution.numEquivDominoPairs(dominoes2)
print(result2)  # Output: 3