# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/

# ============================================
# Reverse Words in a String III
# ============================================
class Solution(object):
    def reverseWords(self, s):
        # Split the sentence into words
        words = s.split(" ")
        # Reverse each word and join them back
        return " ".join([w[::-1] for w in words])

"""
Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for storing reversed words
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    s = "Let's take LeetCode contest"
    print(obj.reverseWords(s))  # Output: "s'teL ekat edoCteeL tsetnoc"
