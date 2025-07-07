# Link: https://leetcode.com/problems/single-number/

#  Single Number
class Solution(object):
    def Test(self, nums):
        hashmap = {x:nums.count(x) for x in nums}
        
        # Finding the key with the minimum value
        min_val = min(hashmap, key=hashmap.get)
        
        return min_val
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    nums = [2,2,1,4,3,5,4,3,5]
    print(obj.Test(nums))

# ----------------------

# Another Solution
class Solution(object):
    def Test(self, nums):
        for i, num in enumerate(nums):
            if num not in nums[: i] and num not in nums[i+1:]:
                return num
            
        return num[0]
                
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    nums = [2,2,1,4,3,5,4,3,5]
    print(obj.Test(nums))

# ----------------------

# Another Solution
class Solution(object):
def Test(self, nums):
    answer = 0
    
    for n in nums:
        answer ^= n
        print(answer)
    
    return answer
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    nums = [2,2,1,4,3,5,4,3,5]
    print(obj.Test(nums))
    

    

