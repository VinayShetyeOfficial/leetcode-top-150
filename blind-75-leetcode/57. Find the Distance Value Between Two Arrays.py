# Link: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/

# Find the Distance Value Between Two Arrays
#  ⭐ Solution 1
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        
        n = len(arr1)
        count = 0
        for x in arr1:
            for y in arr2:
                if abs(x - y) <= d:
                    count += 1
                    break
                
        return n - count  
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    arr1 = [1,4,2,3]
    arr2 = [-4,-3,6,10,20,30]
    d = 3
    print(obj.findTheDistanceValue(arr1, arr2, d))

# ----------------------

# Another Solution
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0
        for num1 in arr1:
            if all(abs(num1 - num2) > d for num2 in arr2):
                count += 1
                
        return count 
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    arr1 = [1,4,2,3]
    arr2 = [-4,-3,6,10,20,30]
    d = 3
    print(obj.findTheDistanceValue(arr1, arr2, d))


