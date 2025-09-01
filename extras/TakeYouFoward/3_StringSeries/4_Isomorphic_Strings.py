# Link: https://takeuforward.org/plus/dsa/problems/isomorphic-string

# Isomorphic String

def isomorphicString(s: str, t: str) -> bool:
    # Two dictionaries to maintain mapping in both directions
    s_to_t_map, t_to_s_map = {}, {}

    for charS, charT in zip(s, t):
        # Check if current mapping contradicts previous mapping
        if (charS in s_to_t_map and s_to_t_map[charS] != charT) or \
           (charT in t_to_s_map and t_to_s_map[charT] != charS):
            return False

        # Store mapping
        s_to_t_map[charS] = charT
        t_to_s_map[charT] = charS

    return True
            

if __name__ == '__main__':
    s = "egg"
    t = "add"
    ans = isomorphicString(s, t) 
    print(f"The two strings are {'not ' if not ans else ''}isomorphic.")  # Output: "isomorphic"

    # Another example
    s2 = "foo"
    t2 = "bar"
    ans2 = isomorphicString(s2, t2)
    print(f"The two strings are {'not ' if not ans2 else ''}isomorphic.")  # Output: "not isomorphic"

"""
Time Complexity (TC): O(N) -> N is the length of the strings
Space Complexity (SC): O(1) -> maximum 256 ASCII characters for mapping
"""
