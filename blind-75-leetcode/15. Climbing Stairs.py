# Link: https://leetcode.com/problems/climbing-stairs/

# Climbing Stairs
class Solution(object):
    def climbStairs(self, n):
        prev_step = 0
        curr_step = 1
        
        for i in range(n):
            next_step = prev_step + curr_step
            prev_step = curr_step
            curr_step = next_step
            
        return curr_step 
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    print(obj.climbStairs(4))
    
