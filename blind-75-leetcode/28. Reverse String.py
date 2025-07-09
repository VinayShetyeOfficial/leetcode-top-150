# Link: https://leetcode.com/problems/reverse-string/description/

# Reverse String
class Solution(object):
    def reverseString(self, s):
        low = 0
        high = len(s)-1
        
        while low <= high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
            
        return s

        # Modify the array in place!
        # s[:] = s[::-1]
        # return s
        # OR
        # return s.reverse()

# Driver code
if __name__ == '__main__':
    obj = Solution()
    s = ["h","e","l","l","o"]
    print(obj.reverseString(s))
