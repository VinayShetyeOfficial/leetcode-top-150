# 67. Add Binary (Easy)
# https://leetcode.com/problems/add-binary - Done

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Adds two binary strings and returns the result as a binary string.
        """

        result = ''
        carry = 0

        # Reverse both strings for easier right-to-left processing
        a, b = a[::-1], b[::-1]

        # Loop through the longer of the two strings
        for i in range(max(len(a), len(b))):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0

            total = digit_a + digit_b + carry
            result = str(total % 2) + result  # Append current binary digit
            carry = total // 2                # Update carry

        # Add final carry if needed
        if carry:
            result = '1' + result

        return result


"""
✅ Time Complexity: O(n)
👉 Where n = max(len(a), len(b))

✅ Space Complexity: O(n)
👉 For the result string
"""
