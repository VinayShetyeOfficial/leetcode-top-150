# Minimum Changes to Make Password Valid

def minChangesToValidPassword(password: str) -> int:
    """
    Problem:
    Given a password string, return the minimum number of changes required 
    such that no two adjacent characters are the same.

    Approach:
    - Traverse the string and check consecutive characters.
    - Maintain a run length for consecutive equal characters.
    - For every run, we need (run_len // 2) changes to break consecutive duplicates.
    - Sum all such required changes.
    """
    
    if not password:
        return 0

    changes = 0
    run_len = 1

    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            run_len += 1
        else:
            changes += run_len // 2
            run_len = 1

    changes += run_len // 2  # Account for last run
    return changes


# 🔽 Test Cases
if __name__ == "__main__":
    test_cases = [
        ("abbbc", 1),    # change one 'b' -> "ababc"
        ("aabbcc", 3),   # need 3 changes to break consecutive pairs
        ("aaa", 1),      # "aaa" -> "aba"
        ("abab", 0),     # already valid
        ("abbaa", 2),    # -> "ababa"
        ("", 0),         # empty string
        ("a", 0),        # single char
        ("aa", 1),       # "aa" -> "ab"
        ("aaaa", 2),     # "aaaa" -> "abab"
    ]

    for i, (password, expected) in enumerate(test_cases, 1):
        result = minChangesToValidPassword(password)
        print(f"Test Case {i}: Input = '{password}'")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass ✅\n" if result == expected else "Fail ❌\n")


"""
Time Complexity (TC):
- O(n), where n = length of the password.
  We make a single pass through the string.

Space Complexity (SC):
- O(1), constant space usage.
  Only counters and variables are used, no extra data structures. 
"""
