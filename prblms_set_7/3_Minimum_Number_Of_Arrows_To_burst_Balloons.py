# 452. Minimum Number of Arrows to Burst Balloons (Medium) - Done
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort by starting x-value
        points.sort()
        arrows = len(points)  # Assume one arrow per balloon initially
        prev = points[0]  # Initialize with the first balloon range

        for i in range(1, len(points)):
            curr = points[i]
            # If overlapping with previous balloon
            if curr[0] <= prev[1]:
                arrows -= 1  # We can reuse the arrow
                # Update the overlap range to the minimum end
                prev = [curr[0], min(prev[1], curr[1])]
            else:
                prev = curr  # No overlap, new arrow needed

        return arrows


"""
✅ Time Complexity: O(n log n)
👉 Sorting takes O(n log n), single scan is O(n)

✅ Space Complexity: O(1)
👉 In-place tracking, no extra structures
"""