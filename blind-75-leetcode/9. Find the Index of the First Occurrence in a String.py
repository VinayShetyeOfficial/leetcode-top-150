# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# Find the Index of the First Occurrence in a String
class Solution(object):
    def strStr(self, haystack, needle):
        # If needle is an empty string, return 0
        if not needle:
            return 0
        
        # Get the length of haystack and needle
        len_h = len(haystack)
        len_n = len(needle)
        
        # Iterate through the haystack
        for i in range(len_h - len_n + 1):
            # Check if the substring of haystack starting at i matches needle
            if haystack[i:i + len_n] == needle:
                return i
        
        # If needle is not found, return -1
        return -1
            

# Driver code
if __name__ == "__main__":
    obj = Solution()

    # Example usage
    haystack1 = "sadbutsad"
    needle1 = "sad"
    print("Index of first occurrence:", obj.strStr(haystack1, needle1))  # Output: 0

    haystack2 = "leetcode"
    needle2 = "leeto"
    print("Index of first occurrence:", obj.strStr(haystack2, needle2))  # Output: -1


"""
===========================================
Time Complexity (TC): O((n-m+1) * m) ~ O(n*m)
- n = length of haystack, m = length of needle
- For each starting index in haystack, we may compare up to m characters.

Space Complexity (SC): O(1)
- No extra space used apart from variables.
===========================================
"""
