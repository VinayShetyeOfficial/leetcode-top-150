# 57. Insert Interval (Medium) - Done
# https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals:
            # Case 1: New interval is completely before the current interval
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[intervals.index(interval):]

            # Case 2: New interval is completely after the current interval
            elif newInterval[0] > interval[1]:
                res.append(interval)

            # Case 3: Overlapping intervals — merge them
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        # Add the merged interval if it hasn’t been added yet
        res.append(newInterval)
        return res


"""
✅ Time Complexity: O(n log n)
👉 Sorting the intervals dominates

✅ Space Complexity: O(n)
👉 For the result list (merged intervals)
"""


