# 198. House Robber (Medium) 
# https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base case: if the list is empty, nothing to rob
        if not nums:
            return 0

        # Initialize two variables:
        # 'loot' is the max money robbed till current house
        # 'skip' is the max money robbed till the previous house
        loot = 0         # Rob current house
        skip = 0         # Skip current house (rob previous)

        for money in nums:
            # If we rob this house, we add current money to skip
            # If we skip this house, take max of previous loot or skip
            new_loot = max(money + skip, loot)
            skip = loot
            loot = new_loot

        return loot

"""
✅ Time Complexity: O(n)
We loop through the list once, where n is the number of houses.

✅ Space Complexity: O(1)
No extra space used. Just two variables are updated in each iteration.
"""

# Alternative Solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_house, adjacent_house = 0, 0

        for val in nums:
            rob_house, adjacent_house = max(val + adjacent_house, rob_house), rob_house
        
        return rob_house
    
    