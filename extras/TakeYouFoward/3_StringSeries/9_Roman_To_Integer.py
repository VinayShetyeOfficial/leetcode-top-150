# Link: https://takeuforward.org/plus/dsa/problems/roman-to-integer

# Convert Roman numeral string to Integer

def roman_to_int(s: str) -> int:
    # Mapping of Roman numerals to integers
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Traverse the Roman numeral from right to left
    for char in reversed(s):
        curr_value = roman_map[char]

        # Subtract if smaller value comes before a larger one
        if curr_value < prev_value:
            total -= curr_value
        else:
            total += curr_value

        prev_value = curr_value

    return total


# Example usage
if __name__ == '__main__':
    string = "LXV"  # 50 + 10 + 5 = 65
    result = roman_to_int(string)
    print(f'Integer value of {string}: {result}')
