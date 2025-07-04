# 42. Trapping Rain Water (Hard) - Done
# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculates the total amount of trapped rainwater given elevation heights.
        Uses two-pointer approach for optimal space and time efficiency.
        """

        if not height:
            return 0

        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        total_water = 0

        # Traverse the elevation map using two pointers
        while left < right:
            if max_left < max_right:
                # Move left pointer inward
                left += 1
                max_left = max(max_left, height[left])
                total_water += max_left - height[left]
            else:
                # Move right pointer inward
                right -= 1
                max_right = max(max_right, height[right])
                total_water += max_right - height[right]

        return total_water


"""
✅ Time Complexity: O(n)
👉 Each element is visited once with two pointers.

✅ Space Complexity: O(1)
👉 No extra space used except for a few variables.
"""

# Alternative SOlution (Somewhat ok)

class Solution:
    def trap(self, height: List[int]) -> int:
        h = len(height)
        maxLeft, maxRight = [0]*h, [0]*h
        l, r = 0, 0
        res = [0]*h
        
        for i in range(h):
             maxLeft[i] = l
             if l < height[i]:
                l = height[i]
        print(maxLeft)
        
        for i in range(h - 1, -1, -1):
            maxRight[i] = r
            if r < height[i]:
                r = height[i]
        print(maxRight)

        for i in range(h):
            unit =  min(maxLeft[i], maxRight[i]) - height[i]
            res[i] = unit if unit > -1 else 0

        print(res)
        
        return sum(res)


"""
✅ Time Complexity: O(n)
👉 Three linear passes: left max, right max, result sum

✅ Space Complexity: O(n)
👉 Two extra arrays (maxLeft and maxRight) of size n
"""