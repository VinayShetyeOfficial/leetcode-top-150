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
                rev_num = (rev_num * 10) + rem
                num //= 10
                
            return x == rev_num
        
if __name__ == "__main__":
    obj = Solution()
    x = 121
    print(obj.isPalindrome(x))

"""
Time Complexity (TC): O(log₁₀(n))  
- We extract digits one by one, so the loop runs proportional to the number of digits in x.  
- For a number with d digits, d = log₁₀(n).

Space Complexity (SC): O(1)  
- Only a few variables (rev_num, rem, num) are used regardless of input size.
"""
