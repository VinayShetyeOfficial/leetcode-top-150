# Link: https://takeuforward.org/plus/dsa/problems/sort-characters-by-frequency

# Sort Characters by Frequency

def frequencySort(s: str) -> list[str]:
    charFreq = {}

    # Step 1: Count frequency
    for ch in s:
        charFreq[ch] = 1 + charFreq.get(ch, 0)

    # Step 2: Sort by (-freq, char) to apply both rules
    result = sorted(charFreq.keys(), key=lambda ch: (-charFreq[ch], ch))

    return result

# Example usage:
if __name__ == '__main__':
    s = "tree"  # {'t': 1, 'r': 1, 'e': 2}
    print(f"Result: {frequencySort(s)}")  # Output: ['e', 'r', 't']

    s2 = "raaaajj"  #{'r': 1, 'a': 4, 'j': 2}
    print(f"Result: {frequencySort(s2)}")  # Output: ['a', 'j', 'r

'''
Note:
We use -charFreq[char] to sort by highest frequency first
The second part char (no -) is used to break ties alphabetically if two characters have the same frequency
'''