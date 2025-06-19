# 125. Valid Palindrome (Easy)
# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Returns True if the string is a palindrome after ignoring
        non-alphanumeric characters and case.
        """

        left, right = 0, len(s) - 1

        while left < right:
            # Move left forward if not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # Move right backward if not alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


"""
✅ Time Complexity: O(n)
👉 n = length of the string

✅ Space Complexity: O(1)
👉 Constant space, two pointers only
"""