# 11. Container With Most Water (Medium) - Done
# https://leetcode.com/problems/container-with-most-water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Finds the maximum amount of water a container can store.
        Uses two-pointer greedy approach to calculate max area.
        """

        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            # Calculate the current container area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            max_area = max(max_area, current_area)

            # Move the pointer with the shorter height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

"""
✅ Time Complexity: O(n)
👉 Each index is visited at most once.

✅ Space Complexity: O(1)
👉 No extra space used beyond variables.
"""
