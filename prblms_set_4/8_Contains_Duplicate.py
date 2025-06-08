# 219. Contains Duplicate II (Easy)
# https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Returns True if there are any duplicate elements such that
        the two indices are at most k apart.
        """

        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i  # Update last seen index

        return False


"""
✅ Time Complexity: O(n)
👉 One pass through the list

✅ Space Complexity: O(n)
👉 In worst case, we store all elements in the hash map
"""