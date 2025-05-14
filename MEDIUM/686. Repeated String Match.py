# 686. Repeated String Match
# Difficulty: Medium

# Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

# Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

 

# Example 1:

# Input: a = "abcd", b = "cdabcdab"
# Output: 3
# Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
# Example 2:

# Input: a = "a", b = "aa"
# Output: 2
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist of lowercase English letters.

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat = a
        count = 1
        while len(repeat) < len(b):
            repeat += a
            count += 1

        if b in repeat:
            return count
        if b in repeat + a:
            return count + 1
        return -1


# Example function call
solution = Solution()

# Example 1
a1 = "abcd"
b1 = "cdabcdab"
result1 = solution.repeatedStringMatch(a1, b1)
print(result1)  # Output: 3

# Example 2
a2 = "a"
b2 = "aa"
result2 = solution.repeatedStringMatch(a2, b2)
print(result2)  # Output: 2