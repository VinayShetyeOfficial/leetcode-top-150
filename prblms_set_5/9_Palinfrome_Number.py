# 9. Palindrome Number (Easy)
# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Checks if an integer is a palindrome by reversing its digits.
        Negative numbers are not palindromes.
        """
        if x < 0:
            return False  # Negative numbers can't be palindromes

        original = x
        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        return reverse == original

"""
✅ Time Complexity: O(log₁₀ n)
👉 One iteration per digit

✅ Space Complexity: O(1)
👉 Constant space, no string conversion
"""