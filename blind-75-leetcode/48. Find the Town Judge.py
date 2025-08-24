# ============================================
# Find the Town Judge - LeetCode
# ============================================

from typing import List
from collections import defaultdict

# ---------------------------
# Solution 1: Using defaultdicts
# ---------------------------
class Solution1:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incomming = defaultdict(int)  # Count of people trusting i
        outgoing = defaultdict(int)   # Count of people i trusts

        for src, dst in trust:
            outgoing[src] += 1
            incomming[dst] += 1

        for i in range(1, n + 1):
            if outgoing[i] == 0 and incomming[i] == n - 1:
                return i
        return -1

"""
Time Complexity (TC): O(T + N) ~ O(T) 
   - T = len(trust), N = number of people
Space Complexity (SC): O(N)
   - For incomming and outgoing dictionaries
"""

# ---------------------------
# Solution 2: Using Lists
# ---------------------------
class Solution2:
    def findJudge(self, n, trust):
        if n == 1:
            return 1  # Only one person, they are the judge

        trusts = [0] * (n + 1)       # Number of people each person trusts
        trusted_by = [0] * (n + 1)   # Number of people trusting each person

        for a, b in trust:
            trusts[a] += 1
            trusted_by[b] += 1

        for i in range(1, n + 1):
            if trusts[i] == 0 and trusted_by[i] == n - 1:
                return i

        return -1

"""
Time Complexity (TC): O(T + N) ~ O(T)
Space Complexity (SC): O(N)
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    n = 3
    trust = [[1,3],[2,3],[3,1]]

    # Test Solution1
    obj1 = Solution1()
    print("Solution1:", obj1.findJudge(n, trust))

    # Test Solution2
    obj2 = Solution2()
    print("Solution2:", obj2.findJudge(n, trust))
