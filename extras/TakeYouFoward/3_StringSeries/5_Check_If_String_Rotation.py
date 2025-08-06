# Link: https://takeuforward.org/plus/dsa/problems/rotate-string

# Check if string `s` can be rotated to form `goal` string

def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal): return False
    
    for shift in range(len(s)):
        rotated = s[shift:] + s[:shift]
        if rotated == goal:
            return True
            
    return False
        
if __name__ == '__main__':
    s = "abcde" 
    goal = "bcdea"
    ans = rotateString(s, goal) 
    print(f"The string `s` can become `goal` string? : {ans}")

