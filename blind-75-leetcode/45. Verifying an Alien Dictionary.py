# ============================================
# Verifying an Alien Dictionary - LeetCode
# ============================================

# ---------------------------
# Solution: Using custom order mapping
# ---------------------------
class Solution(object):
    def isAlienSorted(self, words, order):
        # Map each character to its position in the alien order
        order_index = {char: i for i, char in enumerate(order)}
        
        # Compare two words according to alien dictionary
        def is_sorted(word1, word2):
            for c1, c2 in zip(word1, word2):
                if order_index[c1] < order_index[c2]:
                    return True
                elif order_index[c1] > order_index[c2]:
                    return False
            # If all characters are same so far, shorter word comes first
            return len(word1) <= len(word2)
        
        # Compare each pair of consecutive words
        for i in range(len(words) - 1):
            if not is_sorted(words[i], words[i + 1]):
                return False
        return True

"""
Time Complexity (TC): O(m * n)
   - m = number of words, n = max length of a word
   - Each pair of consecutive words is compared character by character
Space Complexity (SC): O(1)
   - Only a fixed-size dictionary of 26 letters
   - No extra space proportional to input
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    
    print("Result:", obj.isAlienSorted(words, order))  # Output: True
