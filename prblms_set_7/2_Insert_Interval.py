# 57. Insert Interval (Medium) - Done
# https://leetcode.com/problems/insert-interval

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize result with the first interval
        merged = [intervals[0]]

        # Step 3: Iterate through the rest of the intervals
        for start, end in intervals[1:]:
            lastEnd = merged[-1][1]

            # If current interval overlaps with the last one in result
            if start <= lastEnd:
                # Merge by updating the end of last interval
                merged[-1][1] = max(lastEnd, end)
            else:
                # No overlap → add new interval
                merged.append([start, end])

        return merged

"""
✅ Time Complexity: O(n log n)
👉 Sorting the intervals dominates

✅ Space Complexity: O(n)
👉 For the result list (merged intervals)
"""

# Alternate Solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        i = 0

        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]

            # Extend 'end' as long as intervals overlap
            while i + 1 < len(intervals) and intervals[i + 1][0] <= end:
                i += 1
                end = max(end, intervals[i][1])

            res.append([start, end])
            i += 1

        return res


"""
✅ Time Complexity: O(n log n)
👉 Sorting the intervals by start time takes O(n log n)
👉 One pass merging intervals takes O(n)
👉 Total complexity dominated by sorting: O(n log n)


✅ Space Complexity: O(n)
👉 The output list `res` stores the merged intervals and can be up to size n (no merges)
👉 Sorting typically uses O(log n) space due to recursion stack in Timsort (Python’s sort)
👉 Overall space complexity: O(n)
"""