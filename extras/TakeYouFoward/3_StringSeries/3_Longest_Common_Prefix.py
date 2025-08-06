# Link: https://takeuforward.org/plus/dsa/problems/longest-common-prefix

# Longest Common Prefix

def longestCommonPrefix(strings: list[str]) -> str:
    for i in range(len(strings[0])):
        currentChar = strings[0][i]

        for word in strings[1:]:
            if i >= len(word) or word[i] != currentChar:
                return strings[0][:i]
            
    return strings[0]
            
if __name__ == '__main__':
    strings = ["interstellar", "internet", "internal", "intermediate", "intercom", "interview"]
    ans = longestCommonPrefix(strings) # Longest common prefix: intre
    print(f'Longest common prefix: {ans}')