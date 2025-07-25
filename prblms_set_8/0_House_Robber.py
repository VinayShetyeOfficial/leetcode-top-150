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
        # rob_house stores the max amount robbed so far including the current house
        # adjacent_house stores the max amount robbed excluding the current house
        rob_house, adjacent_house = 0, 0

        for money in nums:
            # Update rob_house and adjacent_house based on current house's money
            rob_house, adjacent_house = max(money + adjacent_house, rob_house), rob_house

        # Dry run explanation (for input: [2, 7, 9, 3, 1]):
        # money     | rob_house (after max) | adjacent_house (previous rob_house)
        # --------- | ---------------------- | ----------------------------------
        # 2         | max(2+0, 0) = 2        | 0
        # 7         | max(7+0, 2) = 7        | 2
        # 9         | max(9+2, 7) = 11       | 7
        # 3         | max(3+7, 11) = 11      | 11
        # 1         | max(1+11, 11) = 12     | 11

        return rob_house
    
    