# 13. Roman to Integer (Easy) - Done
# https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to its integer value.
        """

        # Map Roman characters to integer values
        roman_to_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        previous_value = 0

        # Reverse the string to handle subtraction rule naturally
        for char in reversed(s):
            current_value = roman_to_value[char]

            # If current value is less than the previous one, subtract it
            if current_value < previous_value:
                total -= current_value
            else:
                total += current_value

            # Update previous for next iteration
            previous_value = current_value

        return total
    
"""
✅ Time Complexity: O(n)
👉 Where n = length of the Roman numeral string.

✅ Space Complexity: O(1)
👉 Only a dictionary and a few variables are used — no dynamic storage.
"""
