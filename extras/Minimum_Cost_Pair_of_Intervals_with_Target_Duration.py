# Minimum Cost Pair of Intervals with Target Duration

def findMinCost(timeAvl, startTime, endTime, cost):
    n = len(startTime)
    intervals = []

    # Build intervals with their lengths and costs
    for i in range(n):
        length = endTime[i] - startTime[i] + 1
        intervals.append((length, cost[i]))
    print(intervals)
    min_cost = float('inf')

    # Check pairs of intervals
    for i in range(n):
        for j in range(i + 1, n):
            if intervals[i][0] + intervals[j][0] == timeAvl:
                min_cost = min(min_cost, intervals[i][1] + intervals[j][1])

    return min_cost if min_cost != float('inf') else -1


if __name__ == '__main__':
    # Example usage (from Sample Case 0)
    timeAvl_0 = 5
    startTime_0 = [1, 1, 5, 1]
    endTime_0 = [3, 2, 6, 2]
    cost_0 = [4, 5, 1, 4]
    result_0 = findMinCost(timeAvl_0, startTime_0, endTime_0, cost_0)
    print(f"Sample Case 0 Result: {result_0}")

    # Example usage (from Sample Case 1)
    timeAvl_1 = 7
    startTime_1 = [1, 2, 4, 5]
    endTime_1 = [2, 3, 8, 9]
    cost_1 = [2, 3, 4, 10]
    result_1 = findMinCost(timeAvl_1, startTime_1, endTime_1, cost_1)
    print(f"Sample Case 1 Result: {result_1}")

    # Example usage (from Sample Case 2)
    timeAvl_2 = 2
    startTime_2 = [4, 2, 3]
    endTime_2 = [6, 4, 5]
    cost_2 = [3, 1, 4]
    result_2 = findMinCost(timeAvl_2, startTime_2, endTime_2, cost_2)
    print(f"Sample Case 2 Result: {result_2}")
