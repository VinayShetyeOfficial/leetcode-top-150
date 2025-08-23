# ============================================
# Find Smallest Letter Greater Than Target - LeetCode
# ============================================

# ---------------------------
# Solution 1: Binary Search
# ---------------------------
class Solution1(object):
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1
        
        # Edge case: wrap around to first character
        if target >= letters[right]:
            return letters[0]
        
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        # 'left' points to smallest character greater than target
        return letters[left]

"""
Time Complexity (TC): O(log n)
   - Binary search over letters array
Space Complexity (SC): O(1)
   - Constant extra space
"""

# ---------------------------
# Solution 2: Linear Scan
# ---------------------------
class Solution2(object):
    def nextGreatestLetter(self, letters, target):
        for c in letters:
            if c > target:
                return c
        return letters[0]

"""
Time Complexity (TC): O(n)
   - May iterate through all letters in worst case
Space Complexity (SC): O(1)
   - Constant extra space
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    letters = ['a', 'b', 'c', 'e', 'f', 'j', 'z']
    target = "s"
    
    # Test Solution1
    obj1 = Solution1()
    print("Solution1:", obj1.nextGreatestLetter(letters, target))  # Output: 'z'
    
    # Test Solution2
    obj2 = Solution2()
    print("Solution2:", obj2.nextGreatestLetter(letters, target))  # Output: 'z'
