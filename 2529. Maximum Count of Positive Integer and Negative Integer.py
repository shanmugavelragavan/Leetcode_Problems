# 2529. Maximum Count of Positive Integer and Negative Integer
# Difficulty: Easy

# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

 

# Example 1:

# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 2:

# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 3:

# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
 

# Constraints:

# 1 <= nums.length <= 2000
# -2000 <= nums[i] <= 2000
# nums is sorted in a non-decreasing order.
 

# Follow up: Can you solve the problem in O(log(n)) time complexity?

# Solution:

from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        poscount = 0
        negcount = 0

        for num in nums:
            if num > 0:
                poscount += 1
            elif num < 0:
                negcount += 1
        return max(poscount, negcount)

# Example function call
solution = Solution()

# Example 1
nums1 = [-2, -1, -1, 1, 2, 3]
result1 = solution.maximumCount(nums1)
print(result1)  # Output: 3

# Example 2
nums2 = [-3, -2, -1, 0, 0, 1, 2]
result2 = solution.maximumCount(nums2)
print(result2)  # Output: 3

# Example 3
nums3 = [5, 20, 66, 1314]
result3 = solution.maximumCount(nums3)
print(result3)  # Output: 4
