# Link: https://takeuforward.org/plus/dsa/problems/valid-anagram

# Check if two strings are valid anagrams

def anagramStrings(s: str, t: str) -> bool:
    # Strings of different lengths cannot be anagrams
    if len(s) != len(t): 
        return False
    
    # Count frequency of each character in both strings
    s_count, t_count = {}, {}
    for i in range(len(s)):
        s_count[s[i]] = 1 + s_count.get(s[i], 0)
        t_count[t[i]] = 1 + t_count.get(t[i], 0)
        
    # Compare character counts
    for key in s_count:
        if s_count[key] != t_count.get(key, 0):
            return False
            
    return True
        
if __name__ == '__main__':
    s = "dog"
    t = "cat"
    ans = anagramStrings(s, t) 
    print(f"The two strings `s` & `t` are anagrams? : {ans}")  # Output: False

    # Example of anagrams
    s2 = "listen"
    t2 = "silent"
    ans2 = anagramStrings(s2, t2)
    print(f"The two strings `s2` & `t2` are anagrams? : {ans2}")  # Output: True

"""
Time Complexity (TC): O(N) -> Iterate through both strings once
Space Complexity (SC): O(N) -> Two dictionaries to store character counts
"""
