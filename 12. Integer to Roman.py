# 12. Integer to Roman
# Difficulty: Medium

# Seven different symbols represent Roman numerals with the following values:

# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

# If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
# If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
# Given an integer, convert it to a Roman numeral.

 

# Example 1:

# Input: num = 3749

# Output: "MMMDCCXLIX"

# Explanation:

# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
# Example 2:

# Input: num = 58

# Output: "LVIII"

# Explanation:

# 50 = L
#  8 = VIII
# Example 3:

# Input: num = 1994

# Output: "MCMXCIV"

# Explanation:

# 1000 = M
#  900 = CM
#   90 = XC
#    4 = IV
 

# Constraints:

# 1 <= num <= 3999

# Solution:

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
            90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

        result = ''
        for value, symbol in roman_dict.items():
            while num >= value:
                result += symbol
                num -= value

        return result
    
# Create an instance of the Solution class
solution = Solution()

# Example 1: Convert 3749 to a Roman numeral
result1 = solution.intToRoman(3749)
print(result1)  # Output: "MMMDCCXLIX"

# Example 2: Convert 58 to a Roman numeral
result2 = solution.intToRoman(58)
print(result2)  # Output: "LVIII"

# Example 3: Convert 1994 to a Roman numeral
result3 = solution.intToRoman(1994)
print(result3)  # Output: "MCMXCIV"


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Mappings for number to words
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        # Helper function to convert a number less than 1000 to words
        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return less_than_20[n]
            elif n < 100:
                return tens[n // 10] + (" " + less_than_20[n % 10] if n % 10 != 0 else "")
            else:
                return less_than_20[n // 100] + " Hundred" + (" " + helper(n % 100) if n % 100 != 0 else "")
        
        # Split the number into groups of 1000 and process each group
        result = ""
        for i in range(len(thousands)):
            if num % 1000 != 0:
                result = helper(num % 1000) + " " + thousands[i] + " " + result
            num //= 1000
        
        return result.strip()