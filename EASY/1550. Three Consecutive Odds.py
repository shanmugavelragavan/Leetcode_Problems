# 1550. Three Consecutive Odds
# Difficulty: Easy

# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

# Example 1:

# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
# Example 2:

# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.
 

# Constraints:

# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in arr:
            if i % 2 != 0:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False

# Create an instance of the Solution class
solution = Solution()

# Test case 1
arr1 = [2, 6, 4, 1]
print(solution.threeConsecutiveOdds(arr1))  # Output: False

# Test case 2
arr2 = [1, 2, 34, 3, 4, 5, 7, 23, 12]
print(solution.threeConsecutiveOdds(arr2))  # Output: True

# Test case 3
arr3 = [1, 3, 5, 7, 9, 11]  # Three consecutive odds
print(solution.threeConsecutiveOdds(arr3))  # Output: True

# Test case 4
arr4 = [2, 4, 6, 8, 10]  # No consecutive odds
print(solution.threeConsecutiveOdds(arr4))  # Output: False

# Test case 5
arr5 = [1, 1, 1, 1, 1]  # Three consecutive ones
print(solution.threeConsecutiveOdds(arr5))  # Output: True