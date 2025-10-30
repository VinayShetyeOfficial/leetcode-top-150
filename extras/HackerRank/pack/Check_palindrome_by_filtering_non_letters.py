# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/check-palindrome-filter-non-letters

def isAlphabeticPalindrome(code):
    # Write your code here
    res = ''
    
    for char in code:
        res += char.lower() if char.isalpha() else ''
        
    left, right = 0, len(res) - 1

    while left < right:
        if res[left] != res[right]:
            return False
            
        left += 1
        right -= 1
        
    return True
    
print(isAlphabeticPalindrome('abc124cba'))
    
    
