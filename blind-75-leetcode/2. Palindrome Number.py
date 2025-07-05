# Link: https://leetcode.com/problems/palindrome-number/description/

# Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        num = x
        rev_num = 0
        
        if num < 0:
            return False
        else:
            while num:
                rem = num % 10
                rev_num = (rev_num*10) + rem
                num //= 10
                
            return x == rev_num
        
if __name__ == "__main__":
    obj = Solution()
    x = 121
    print(obj.isPalindrome(x))