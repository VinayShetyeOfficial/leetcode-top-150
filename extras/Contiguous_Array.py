# 525. Contiguous Array (Medium) - Done
# https://leetcode.com/problems/contiguous-array

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count, max_len = 0, 0
        seen = {0:-1}

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count in seen:
                max_len = max(max_len, i - seen[count])
            else:
                seen[count] = i
        
        return max_len
    
"""
🕒 Time and Space Complexity:
Time Complexity: O(n)

Space Complexity: O(n) (for the hashmap seen)
"""