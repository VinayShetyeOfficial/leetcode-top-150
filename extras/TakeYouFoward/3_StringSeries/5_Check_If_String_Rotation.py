# Link: https://takeuforward.org/plus/dsa/problems/rotate-string

# Check if string `s` can be rotated to form `goal` string

def rotateString(s: str, goal: str) -> bool:
    # Strings of different lengths cannot be rotations of each other
    if len(s) != len(goal): 
        return False
    
    # Try all possible rotations
    for shift in range(len(s)):
        rotated = s[shift:] + s[:shift]
        if rotated == goal:
            return True
            
    return False
        
if __name__ == '__main__':
    s = "abcde" 
    goal = "bcdea"
    ans = rotateString(s, goal) 
    print(f"The string `s` can become `goal` string? : {ans}")  # Output: True

    # Another example
    s2 = "abcde"
    goal2 = "abced"
    ans2 = rotateString(s2, goal2)
    print(f"The string `s` can become `goal` string? : {ans2}")  # Output: False

"""
Time Complexity (TC): O(N^2) -> For each of N shifts, slicing and concatenation takes O(N)
Space Complexity (SC): O(N) -> for storing rotated string in each iteration
"""
