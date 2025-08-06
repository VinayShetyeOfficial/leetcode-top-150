# Link: https://takeuforward.org/plus/dsa/problems/isomorphic-string

# Isomorphic String

def isomorphicString(s: str, t: str) -> bool:
    s_to_t_map, t_to_s_map = {}, {}

    for charS, charT in zip(s, t):
        if (charS in s_to_t_map and s_to_t_map[charS] != charT) or \
           (charT in t_to_s_map and t_to_s_map[charT] != charS):
            return False
        s_to_t_map[charS] = charT
        t_to_s_map[charT] = charS

    return True
            
if __name__ == '__main__':
    s = "egg"
    t = "add"
    ans = isomorphicString(s, t) 
    print(f"The two strings are {'not ' if not ans else ''}isomorphic.")
