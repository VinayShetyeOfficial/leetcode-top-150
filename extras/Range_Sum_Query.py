# 303. Range Sum Query - Immutable (Easy) - Done
# https://leetcode.com/problems/range-sum-query-immutable

def get_prefix_sum(arr):
    running_sum = 0
    for index, number in enumerate(arr):
        running_sum += number
        arr[index] = running_sum
    
    return arr

nums = [1, 2, 3, 4, 5, 6]
print(get_prefix_sum(nums))

"""
Time Complexity: O(n)
- We go through each element in the list exactly once.
- Each operation inside the loop is O(1), so the total time is linear in the size of the input array.

Space Complexity: O(1)
- No extra space is used except for a few variables like `running_sum`, `index`, and `number`.
- We're modifying the input list in-place, so no new list is created.

If you want to preserve the original list, then space complexity would become O(n).
"""


