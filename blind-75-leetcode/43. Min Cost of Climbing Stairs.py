# https://leetcode.com/problems/min-cost-climbing-stairs/description/

# Min Cost of Climbing Stairs

class Solution(object):
    def minCostClimbingStairs(self, cost):
        if not cost:
            return 0
        
        dp0, dp1 = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            current_cost = cost[i]
            current_min_cost = current_cost + min(dp0, dp1)
            dp0, dp1 = dp1, current_min_cost
        
        return min(dp0, dp1)
           
# Driver code
if __name__ == '__main__':
    obj = Solution()
    
    cost = [1,100,1,1,1,100,1,1,100,1]
    print(obj.minCostClimbingStairs(cost))

# Another Solution

# =======================================================

class Solution(object):
    def minCostClimbingStairs(self, cost):
        
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        print(cost)
        
        return min(cost[0], cost[1])
           
# Driver code
if __name__ == '__main__':
    obj = Solution()
    
    cost = [1,100,1,1,1,100,1,1,100,1]
    print(obj.minCostClimbingStairs(cost))

    