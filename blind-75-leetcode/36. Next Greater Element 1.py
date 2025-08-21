# Link: https://leetcode.com/problems/next-greater-element-i/description/

# ============================================
# Solution 1: Brute-force approach
# ============================================
class Solution1(object):
    def nextGreaterElement(self, nums1, nums2):
        res = []
        
        for x in nums1:
            found = False
            # Start searching in nums2 right after the current element x
            for y in nums2[nums2.index(x)+1:]:
                if y > x:
                    res.append(y)
                    found = True
                    break
            
            if not found:
                res.append(-1)       
                
        return res

"""
Time Complexity: O(m * n), where m = len(nums1), n = len(nums2)
Space Complexity: O(m) for the result list
"""

# ============================================
# Solution 2: Using Stack (Optimal)
# ============================================
class Solution2(object):
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}
        stack = []
        
        # Traverse nums2 from left to right
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        
        # Remaining elements have no next greater
        for num in stack:
            next_greater[num] = -1
        
        # Build result for nums1
        return [next_greater[x] for x in nums1]

"""
Time Complexity: O(n + m), where n = len(nums2), m = len(nums1)
Space Complexity: O(n) for stack and hashmap
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]

    obj1 = Solution1()
    print("Next Greater Elements (Brute-force):", obj1.nextGreaterElement(nums1, nums2))

    obj2 = Solution2()
    print("Next Greater Elements (Stack-based):", obj2.nextGreaterElement(nums1, nums2))
