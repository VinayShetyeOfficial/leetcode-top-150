# Minimum Changes to Make Password Valid

def minChangesToValidPassword(password: str) -> int:
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

    changes += run_len // 2  # last run
    return changes

# Tests
print(minChangesToValidPassword("abbbc"))   # 1  (ababc)
print(minChangesToValidPassword("aabbcc"))  # 3
print(minChangesToValidPassword("aaa"))     # 1
print(minChangesToValidPassword("abab"))    # 0
print(minChangesToValidPassword("abbaa"))   # 2
