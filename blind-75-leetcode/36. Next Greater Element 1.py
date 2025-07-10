# Link: https://leetcode.com/problems/next-greater-element-i/description/

# Next Greater Element 1
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        res = []
        
        for x in nums1:
            found = False
            for y in nums2[nums2.index(x)+1:]:
                if y > x:
                    res += [y]
                    found = True
                    break
            
            if not found:
                res += [-1]       
                
        return res
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    print(obj.nextGreaterElement(nums1, nums2))




