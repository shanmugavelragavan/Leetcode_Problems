# 9. Palindrome Number
# Difficulty: Easy

# Given an integer x, return true if x is a palindrome, and false otherwise.




# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?

# Solution:

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
    


# Create an instance of the Solution class
solution = Solution()

# Example 1: Check if 121 is a palindrome
result1 = solution.isPalindrome(121)
print(result1)  # Output: True

# Example 2: Check if -121 is a palindrome
result2 = solution.isPalindrome(-121)
print(result2)  # Output: False

# Example 3: Check if 10 is a palindrome
result3 = solution.isPalindrome(10)
print(result3)  # Output: False
