# Link: https://takeuforward.org/plus/dsa/problems/longest-common-prefix

# Longest Common Prefix

def longestCommonPrefix(strings: list[str]) -> str:
    if not strings:
        return ""

    for i in range(len(strings[0])):
        currentChar = strings[0][i]

        for word in strings[1:]:
            # Stop if current index is out of range or character mismatch
            if i >= len(word) or word[i] != currentChar:
                return strings[0][:i]
            
    return strings[0]  # All characters matched in all strings
            
if __name__ == '__main__':
    strings = ["interstellar", "internet", "internal", "intermediate", "intercom", "interview"]
    ans = longestCommonPrefix(strings)
    print(f'Longest common prefix: {ans}')  # Output: "inter"

"""
Time Complexity (TC): O(N * M) -> N: number of strings, M: length of first string (worst case)
Space Complexity (SC): O(1) -> only using a few variables
"""
