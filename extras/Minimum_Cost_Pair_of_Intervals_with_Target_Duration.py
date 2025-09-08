# Minimum Cost Pair of Intervals with Target Duration

def findMinCost(timeAvl, startTime, endTime, cost):
    """
    Problem:
    Given n intervals with startTime, endTime, and cost, find the minimum cost
    to pick two intervals such that their total duration equals timeAvl.

    Approach:
    - Calculate length of each interval: length = endTime[i] - startTime[i] + 1
    - Check all pairs of intervals to see if their total length equals timeAvl.
    - Keep track of minimum sum of their costs.
    """
    
    n = len(startTime)
    intervals = []

    # Build intervals with their lengths and costs
    for i in range(n):
        length = endTime[i] - startTime[i] + 1
        intervals.append((length, cost[i]))
    # print(intervals)  # Debugging removed for final version
    min_cost = float('inf')

    # Check pairs of intervals
    for i in range(n):
        for j in range(i + 1, n):
            if intervals[i][0] + intervals[j][0] == timeAvl:
                min_cost = min(min_cost, intervals[i][1] + intervals[j][1])

    return min_cost if min_cost != float('inf') else -1


# 🔽 Test Cases
if __name__ == '__main__':
    test_cases = [
        # (timeAvl, startTime, endTime, cost, expected)
        (5, [1, 1, 5, 1], [3, 2, 6, 2], [4, 5, 1, 4], 2),
        (7, [1, 2, 4, 5], [2, 3, 8, 9], [2, 3, 4, 10], 6),
        (2, [4, 2, 3], [6, 4, 5], [3, 1, 4], -1),
        (4, [1,2,3], [2,3,4], [1,2,3], 3),  # 2+2=4, cost 1+2=3
        (3, [1,1,2], [1,2,3], [5,3,4], 8),  # Only one pair sum 3
    ]

    for i, (timeAvl, startTime, endTime, cost, expected) in enumerate(test_cases, 1):
        result = findMinCost(timeAvl, startTime, endTime, cost)
        print(f"Test Case {i}: Expected = {expected}, Got = {result}")
        print("Pass ✅\n" if result == expected else "Fail ❌\n")

"""
Time Complexity (TC):
- O(n^2), where n = number of intervals.
  We check all pairs of intervals.

Space Complexity (SC):
- O(n), for storing intervals with their lengths and costs.
"""