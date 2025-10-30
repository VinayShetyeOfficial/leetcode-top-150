# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/check-non-identical-string-rotation

def isNonTrivialRotation(s1, s2):
    # Write your code here
    if len(s1) != len(s2) or s1 == s2: 
        return 0
    
    string = ''
    for index in range(len(s1)):
        string = s1[index: ] + s1[:index]
        if string == s2:
            return 1
            
    return 0
