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
    s = "tree"
    print(f"Result: {frequencySort(s)}")  # Output: ['e', 'r', 't']

    s2 = "raaaajj"
    print(f"Result: {frequencySort(s2)}")  # Output: ['a', 'j', 'r']
