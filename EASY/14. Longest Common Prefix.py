# 14. Longest Common Prefix
# Difficulty: Easy

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution:
  def longestCommonPrefix(self, strs):
    prefix = ""
    for i in range(len(strs[0])):
      for s in strs:
        if i == len(s) or s[i] != strs[0][i]:
          return prefix
      prefix += strs[0][i]
    return prefix

# Create an instance of the Solution class
solution = Solution()

# Test case 1
strs1 = ["flower", "flow", "flight"]
result1 = solution.longestCommonPrefix(strs1)
print(result1)  # Output: "fl"

# Test case 2
strs2 = ["dog", "racecar", "car"]
result2 = solution.longestCommonPrefix(strs2)
print(result2)  # Output: ""


