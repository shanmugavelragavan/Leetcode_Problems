# 2094. Finding 3-Digit Even Numbers
# Difficulty: Easy

# You are given an integer array digits, where each element is a digit. The array may contain duplicates.

# You need to find all the unique integers that follow the given requirements:

# The integer consists of the concatenation of three elements from digits in any arbitrary order.
# The integer does not have leading zeros.
# The integer is even.
# For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

# Return a sorted array of the unique integers.

 

# Example 1:

# Input: digits = [2,1,3,0]
# Output: [102,120,130,132,210,230,302,310,312,320]
# Explanation: All the possible integers that follow the requirements are in the output array. 
# Notice that there are no odd integers or integers with leading zeros.
# Example 2:

# Input: digits = [2,2,8,8,2]
# Output: [222,228,282,288,822,828,882]
# Explanation: The same digit can be used as many times as it appears in digits. 
# In this example, the digit 8 is used twice each time in 288, 828, and 882. 
# Example 3:

# Input: digits = [3,7,5]
# Output: []
# Explanation: No even integers can be formed using the given digits.
 

# Constraints:

# 3 <= digits.length <= 100
# 0 <= digits[i] <= 9

from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # Get all possible 3-digit combinations
        result = set()
        for p in permutations(digits, 3):
            # Skip if leading zero
            if p[0] == 0:
                continue
            # Create number and check if even
            num = p[0] * 100 + p[1] * 10 + p[2]
            if num % 2 == 0:
                result.add(num)
        
        return sorted(list(result))

# Create an instance of the Solution class
solution = Solution()

# Test case 1
digits1 = [2, 1, 3, 0]
print(solution.findEvenNumbers(digits1))  # Output: [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]

# Test case 2
digits2 = [2, 2, 8, 8, 2]
print(solution.findEvenNumbers(digits2))  # Output: [222, 228, 282, 288, 822, 828, 882]

# Test case 3
digits3 = [3, 7, 5]
print(solution.findEvenNumbers(digits3))  # Output: []