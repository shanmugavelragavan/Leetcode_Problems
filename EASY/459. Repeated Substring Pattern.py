# 459. Repeated Substring Pattern
# Difficulty: Easy

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if s in s[1:] + s[:-1]:
            return True
        else:
            return False

# Example function call
solution = Solution()

# Example 1
s1 = "abab"
result1 = solution.repeatedSubstringPattern(s1)
print(result1)  # Output: True

# Example 2
s2 = "aba"
result2 = solution.repeatedSubstringPattern(s2)
print(result2)  # Output: False

# Example 3
s3 = "abcabcabcabc"
result3 = solution.repeatedSubstringPattern(s3)
print(result3)  # Output: True
