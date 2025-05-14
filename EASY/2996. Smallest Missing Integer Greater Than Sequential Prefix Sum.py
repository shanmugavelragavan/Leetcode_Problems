# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
# Difficulty: Easy

# You are given a 0-indexed array of integers nums.

# A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.

# Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.



# Example 1:

# Input: nums = [1,2,3,2,5]
# Output: 6
# Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
# Example 2:

# Input: nums = [3,4,5,1,12,14,13]
# Output: 15
# Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

# Constraints:

# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
      # Find the longest sequential prefix
        prefix_sum = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i-1] + 1:
            prefix_sum += nums[i]
            i += 1
      # Find the smallest missing integer greater than or equal to the sum of the longest sequential prefix
        x = prefix_sum
        while x in nums:
            x += 1
        return x


# Example function call
solution = Solution()

# Example 1
nums1 = [1,2,3,2,5]
result1 = solution.missingInteger(nums1)
print(result1)  # Output: 6

# Example 2
nums2 = [3,4,5,1,12,14,13]
result2 = solution.missingInteger(nums2)
print(result2)  # Output: 15

