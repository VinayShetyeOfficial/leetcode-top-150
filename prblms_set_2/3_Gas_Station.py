# 134. Gas Station (Medium) - Done
# https://leetcode.com/problems/gas-station/description/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Returns the index of the gas station to start from in order to complete the circuit.
        If not possible, returns -1.
        """

        # If total gas is less than total cost, it is impossible to complete the circuit
        if sum(gas) < sum(cost):
            return -1

        total_fuel = 0       # Tracks fuel in tank during traversal
        starting_station = 0  # Index from which we attempt to start the journey

        # Try to find a valid starting station
        for i in range(len(gas)):
            total_fuel += gas[i] - cost[i]

            # If at any point, fuel in tank is negative, we can't start from previous station(s)
            if total_fuel < 0:
                # Reset tank and try next station as starting point
                total_fuel = 0
                starting_station = i + 1

        return starting_station

"""
✅ Time Complexity: O(n)
👉 We iterate through the list once.

✅ Space Complexity: O(1)
👉 Only a few variables are used — no extra data structures.
"""