# 415. Add Strings
# Difficulty: Easy

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"
 

# Constraints:

# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(num1[i])
                i -= 1
            if j >= 0:
                carry += int(num2[j])
                j -= 1
            result.append(str(carry % 10))
            carry //= 10

        return ''.join(result[::-1])

# Test cases
solution = Solution()
print(solution.addStrings("11", "123"))  # Output: "134"
print(solution.addStrings("456", "77"))    # Output: "533"
print(solution.addStrings("0", "0"))       # Output: "0"