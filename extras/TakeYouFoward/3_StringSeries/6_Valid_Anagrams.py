# Valid Anagrams

def anagramStrings(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    
    s_count, t_count = {}, {}
    for i in range(len(s)):
        s_count[s[i]] = 1 + s_count.get(s[i], 0)
        t_count[t[i]] = 1 + t_count.get(t[i], 0)
        
    for key in s_count:
        if s_count[key] != t_count.get(key, 0):
            return False
            
    return True
        
        
if __name__ == '__main__':
    s = "dog"
    t = "cat"
    ans = anagramStrings(s, t) 
    print(f"The two strings `s` & `t` are anagrams? : {ans}")

