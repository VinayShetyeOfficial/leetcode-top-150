# 151. Reverse Words in a String (Medium) - Done
# https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverses the words in the input string s, removing extra spaces.
        Returns a single space-separated string with words in reverse order.
        """

        # Step 1: Split words by whitespace and filter out empty strings
        words = s.strip().split()

        # Step 2: Reverse the list of words
        reversed_words = words[::-1]

        # Step 3: Join them with a single space
        return ' '.join(reversed_words)

"""
✅ Time Complexity: O(n)
👉 Where n is the number of characters in the input string.

✅ Space Complexity: O(n)
👉 Because of the list of words and the output string.
"""

# Alternative Solution:
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverses the words in the input string s, removing extra spaces.
        Returns a single space-separated string with words in reverse order.
        """
        return ' '.join(s.split()[::-1])
  