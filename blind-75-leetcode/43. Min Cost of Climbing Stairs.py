# ============================================
# Min Cost Climbing Stairs - LeetCode
# ============================================

# ---------------------------
# Solution 1: Bottom-up DP with two variables (space optimized)
# ---------------------------
class Solution1(object):
    def minCostClimbingStairs(self, cost):
        if not cost:
            return 0
        
        dp0, dp1 = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            current_cost = cost[i]
            current_min_cost = current_cost + min(dp0, dp1)
            dp0, dp1 = dp1, current_min_cost
        
        return min(dp0, dp1)

"""
Time Complexity (TC): O(n)
   - Traverse the cost array once
Space Complexity (SC): O(1)
   - Only two variables used to store previous costs
"""

# ---------------------------
# Solution 2: In-place DP (modifying cost array)
# ---------------------------
class Solution2(object):
    def minCostClimbingStairs(self, cost):
        # Update cost array from second last step backwards
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        # Minimum cost starting from step 0 or 1
        return min(cost[0], cost[1])

"""
Time Complexity (TC): O(n)
   - Traverse the cost array once in reverse
Space Complexity (SC): O(1)
   - No extra space used, modifying input array in-place
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    cost = [1,100,1,1,1,100,1,1,100,1]
    
    # Test Solution1
    obj1 = Solution1()
    print("Solution1:", obj1.minCostClimbingStairs(cost.copy()))
    
    # Test Solution2
    obj2 = Solution2()
    print("Solution2:", obj2.minCostClimbingStairs(cost.copy()))
