# 560. Subarray Sum Equals K (Medium)
# https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSum = {0: 1}  # base case: one subarray starts at index 0

        for n in nums:
            curSum += n
            diff = curSum - k

            # if we've seen this difference before, we found a valid subarray
            res += prefixSum.get(diff, 0)

            # record the current sum
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return res
    
"""
🕒 Time & Space:
Time Complexity: O(n)

Space Complexity: O(n) (for hashmap)
"""
