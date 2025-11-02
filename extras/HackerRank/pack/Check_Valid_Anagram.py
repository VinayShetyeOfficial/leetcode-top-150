# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/check-valid-anagram

def isAnagram(s, t):
    # Write your code here
    if len(s) != len(t): return 0
    
    countS, countT = {}, {}
    
    for charS, charT in zip(s, t):
        countS[charS] = 1 + countS.get(charS, 0)
        countT[charT] = 1 + countT.get(charT, 0)
    
    for char, freq in countS.items():
        if freq != countT.get(char, 0):
            return 0
            
    return 1 