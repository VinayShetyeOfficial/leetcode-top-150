# Link: https://leetcode.com/problems/first-bad-version/description/

# ============================================
# Simulating the isBadVersion API
# ============================================

def isBadVersion(version):
    # Assume the first bad version is 10 for testing
    first_bad_version = 10
    return version >= first_bad_version

# ============================================
# Solution using Binary Search
# ============================================

class Solution(object):
    def firstBadVersion(self, n):
        low = 1
        high = n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low

"""
Time Complexity: O(log n)
    - Binary search halves the search space each step.
Space Complexity: O(1)
    - Only a few variables (low, high, mid) are used.
"""

# ============================================
# Driver code
# ============================================

if __name__ == '__main__':
    obj = Solution()
    n = 20  # Example number of versions
    print("First bad version is:", obj.firstBadVersion(n))
