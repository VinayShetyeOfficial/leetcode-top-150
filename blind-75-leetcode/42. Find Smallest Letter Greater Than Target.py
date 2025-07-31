# Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

# Find Smallest Letter Greater Than Target
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1
        
        # Edge case: If target is greater than or equal to the last character,
        # wrap around to the first character
        if target >= letters[right]:
            return letters[0]
        
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        # After binary search, 'left' will point to the smallest character greater than target
        return letters[left]
            
# Driver code
if __name__ == '__main__':
    obj = Solution()
    
    letters = ['a', 'b', 'c', 'e', 'f', 'j', 'z']
    target = "s"
    print(obj.nextGreatestLetter(letters, target))


# ============================================

# Another Solution

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        charArr = letters
        
        for c in charArr:
            if c > target:
                return c
        
        return letters[0]
            
# Driver code
if __name__ == '__main__':
    obj = Solution()
    
    letters = ['a', 'b', 'c', 'e', 'f', 'j', 'z']
    target = "s"
    print(obj.nextGreatestLetter(letters, target))
    