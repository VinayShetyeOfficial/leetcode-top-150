# Link: https://leetcode.com/problems/first-bad-version/description/

# First Bad Version
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# Simulating the isBadVersion API
def isBadVersion(version):
    # Assume the first bad version is randomly chosen for this example
    first_bad_version = 10  # Example: set it to 10 for consistency in testing
    return version >= first_bad_version

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

# Driver code
if __name__ == '__main__':
    obj = Solution()
    n = 20  # Example number of versions
    print("First bad version is:", obj.firstBadVersion(n))
