# 135. Candy (Hard) - Done
# https://leetcode.com/problems/candy

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Returns the minimum number of candies required to distribute to children,
        satisfying the rules based on their ratings.
        """

        n = len(ratings)
        candies = [1] * n  # Step 1: Every child gets at least 1 candy

        # Step 2: Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Step 4: Total candies required
        return sum(candies)

"""
✅ Time Complexity: O(n)
👉 Two passes through the array: left → right and right → left.

✅ Space Complexity: O(n)
👉 We use an additional list of size n to store candies.
"""

# Alternative Solution (Easy Variables):
class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                arr[i] = arr[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if  ratings[i] > ratings[i + 1]:
                arr[i] = max(arr[i], arr[i + 1] + 1)
        
        return sum(arr)

"""
✅ Time Complexity: O(n)
👉 Two linear passes over the list

✅ Space Complexity: O(n)
👉 Extra array `arr` stores candies for each child
"""
