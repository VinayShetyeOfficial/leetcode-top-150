# Link: `

# Find the Town Judge
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incomming = defaultdict(int)
        outgoing = defaultdict(int) 

        for src, dst in trust:
            outgoing[src] += 1
            incomming[dst] += 1

        for i in range(1, n + 1):
            if outgoing[i] == 0 and incomming[i] == n - 1:
                return i
        return -1


=============================================================
class Solution(object):
    def findJudge(self, n, trust):
        # Special case: if only one person in the town
        if n == 1:  
            return 1
        
        trusts = [0] * (n + 1)
        trusted_by = [0] * (n + 1)
        
        for a, b in trust:
            trusts[a] += 1
            trusted_by[b] += 1
        print("Trusts: ", trusts)
        print("Trusted_By: ", trusted_by)

        
        for i in range(1, n + 1):
            if trusts[i] == 0 and trusted_by[i] == n - 1:
                return i
        
        return -1
                   
# Driver code
if __name__ == '__main__':
    obj = Solution()
    n = 3
    trust =   [[1,3],[2,3],[3,1]]
    print(obj.findJudge(n, trust))
    