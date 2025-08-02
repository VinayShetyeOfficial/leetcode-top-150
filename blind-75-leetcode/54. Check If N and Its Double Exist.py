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

'''
# Explanation
-------------
1. num * 2 in seen
This checks if current number is half of any number seen before.
Example: if we already saw 10, and now we see 5 → 5 * 2 = 10 → ✅ Match!


2. (num % 2 == 0 and num // 2 in seen)
This part checks if the current number is double of a number seen before.

BUT — we must only check this when the number is even, because odd numbers don’t have exact integer halves.

That’s why:
num % 2 == 0 → ensures the number is divisible by 2.
num // 2 in seen → checks if we’ve already seen a number that is exactly half of current.
'''