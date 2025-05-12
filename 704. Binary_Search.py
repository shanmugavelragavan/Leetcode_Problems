# 704. Binary Search
# Difficulty: Easy

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

# Solution:

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
        return -1
    
# Create an instance of the Solution class
solution = Solution()

# Test case 1
nums1 = [-1, 0, 3, 5, 9, 12]
target1 = 9
result1 = solution.search(nums1, target1)
print(result1)  # Output: 4

# Test case 2
nums2 = [-1, 0, 3, 5, 9, 12]
target2 = 2
result2 = solution.search(nums2, target2)
print(result2)  # Output: -1
