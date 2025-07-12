# Link: https://leetcode.com/problems/check-if-n-and-its-double-exist/description/

# Check If N and Its Double Exist
class Solution(object):
    def checkIfExist(self, arr):
        seen = set()
        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    arr = [-2,0,10,-19,4,6,-8]
    print(obj.checkIfExist(arr))
    