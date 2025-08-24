# ============================================
# Check If N and Its Double Exist - LeetCode
# ============================================

class Solution(object):
    def checkIfExist(self, arr):
        seen = set()
        for num in arr:
            # Check if double or half (if even) exists in seen
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    arr = [-2, 0, 10, -19, 4, 6, -8]
    print(obj.checkIfExist(arr))  # Output: False

"""
Time Complexity (TC): O(n)
- n: number of elements in arr
- We iterate through array once, each lookup in set is O(1)

Space Complexity (SC): O(n)
- Space used by 'seen' set storing at most n elements
"""
