# 12. Integer to Roman (Medium) - Done
# https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Converts an integer to its Roman numeral representation.
        Uses a greedy approach based on descending Roman value-symbol pairs.
        """

        # List of (value, symbol) pairs in descending order
        value_symbol_pairs = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        roman_result = []

        # Iterate through each value-symbol pair
        for value, symbol in value_symbol_pairs:
            while num >= value:
                roman_result.append(symbol)  # Append symbol
                num -= value                 # Subtract its value

        return ''.join(roman_result)


"""
✅ Time Complexity: O(1)
👉 Max number is 3999 → fixed number of steps

✅ Space Complexity: O(1)
👉 Output string is of bounded length (at most ~15 characters for 3999)
"""