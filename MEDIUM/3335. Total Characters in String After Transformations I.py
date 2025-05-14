# 3335. Total Characters in String After Transformations I
# Difficulty: Medium

# You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

# If the character is 'z', replace it with the string "ab".
# Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
# Return the length of the resulting string after exactly t transformations.

# Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: s = "abcyy", t = 2

# Output: 7

# Explanation:

# First Transformation (t = 1):
# 'a' becomes 'b'
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'y' becomes 'z'
# 'y' becomes 'z'
# String after the first transformation: "bcdzz"
# Second Transformation (t = 2):
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'd' becomes 'e'
# 'z' becomes "ab"
# 'z' becomes "ab"
# String after the second transformation: "cdeabab"
# Final Length of the string: The string is "cdeabab", which has 7 characters.
# Example 2:

# Input: s = "azbk", t = 1

# Output: 5

# Explanation:

# First Transformation (t = 1):
# 'a' becomes 'b'
# 'z' becomes "ab"
# 'b' becomes 'c'
# 'k' becomes 'l'
# String after the first transformation: "babcl"
# Final Length of the string: The string is "babcl", which has 5 characters.
 

# Constraints:

# 1 <= s.length <= 105
# s consists only of lowercase English letters.
# 1 <= t <= 105

# Slow Solution

# from collections import deque

# class Solution:
#     def lengthAfterTransformations(self, s: str, t: int) -> int:
#         MOD = 10 ** 9 + 7

#         queue = deque()
#         for ch in s:
#             queue.append((ch, t))

#         total = 0
#         while queue:
#             ch, time = queue.popleft()
#             if time == 0:
#                 total = (total + 1) % MOD
#             else:
#                 if ch == 'z':
#                     queue.append(('a', time - 1))
#                     queue.append(('b', time - 1))
#                 else:
#                     next_ch = chr(ord(ch) + 1)
#                     queue.append((next_ch, time - 1))

#         return total


# Time Limit Exceeded Solution

# from functools import lru_cache

# class Solution:
#     def lengthAfterTransformations(self, s: str, t: int) -> int:
#         MOD = 10**9 + 7

#         @lru_cache(maxsize=None)
#         def get_length(ch: str, time: int) -> int:
#             if time == 0:
#                 return 1
#             if ch == 'z':
                # 'z' becomes 'ab'
        #         return (get_length('a', time - 1) + get_length('b', time - 1)) % MOD
        #     else:
        #         next_ch = chr(ord(ch) + 1)
        #         return get_length(next_ch, time - 1) % MOD

        # total = 0
        # for ch in s:
        #     total = (total + get_length(ch, t)) % MOD
        # return total


# Memory Limit Exceeded Solution

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        
        # Count of each character a-z at time 0
        from collections import Counter
        count = [0] * 26  # index 0='a', 1='b', ..., 25='z'
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for _ in range(t):
            new_count = [0] * 26
            for i in range(26):
                if i == 25:  # 'z'
                    new_count[0] = (new_count[0] + count[25]) % MOD  # 'a'
                    new_count[1] = (new_count[1] + count[25]) % MOD  # 'b'
                else:
                    new_count[i + 1] = (new_count[i + 1] + count[i]) % MOD
            count = new_count
        
        return sum(count) % MOD


# Test cases
solution = Solution()
print(solution.lengthAfterTransformations("abcyy", 2))   # Output: 7
print(solution.lengthAfterTransformations("azbk", 1))    # Output: 5
print(solution.lengthAfterTransformations("jqktcurgdvlibczdsvnsg", 7517))  # Fast & correct
print(solution.lengthAfterTransformations("dcmmcvbhgkdhtlxglsnoijmrrdaiaksnbms", 8895))  # Works fast & within memory
