# Link: https://takeuforward.org/plus/dsa/problems/sort-characters-by-frequency

# Sort characters in a string based on their frequency in descending order

def frequencySort(s: str) -> str:
    charFreq = {}

    # Step 1: Count frequency of each character
    for ch in s:
        charFreq[ch] = 1 + charFreq.get(ch, 0)

    # Step 2: Sort characters by frequency (descending) and then by character (ascending)
    sorted_chars = sorted(charFreq.keys(), key=lambda ch: (-charFreq[ch], ch))

    # Step 3: Build result string with each character repeated by its frequency
    result = ''.join(ch * charFreq[ch] for ch in sorted_chars)

    return result

# Example usage
if __name__ == '__main__':
    s = "tree"  # {'t':1, 'r':1, 'e':2}
    print(f"Sorted by frequency: {frequencySort(s)}")  # Output: 'eert' or 'eetr'

    s2 = "raaaajj"  # {'r':1, 'a':4, 'j':2}
    print(f"Sorted by frequency: {frequencySort(s2)}")  # Output: 'aaaajj r'

'''
Note:
- Sorting by -charFreq[ch] ensures highest frequency characters come first.
- Sorting by character itself resolves ties alphabetically.
- Time Complexity: O(N + K log K), N=len(s), K=unique characters
- Space Complexity: O(K)
'''
