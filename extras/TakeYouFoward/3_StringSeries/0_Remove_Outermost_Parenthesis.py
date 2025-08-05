# Link: https://takeuforward.org/plus/dsa/problems/remove-outermost-parentheses

# Remove Outermost Parentheses

def removeOuterParentheses(s: str) -> str:
    result = []
    balance = 0
    start = 0

    for i in range(len(s)):
        if s[i] == '(':
            balance += 1
        else:
            balance -= 1

        # If balance is 0, we found a primitive component
        if balance == 0:
            # Add the content inside the outermost parentheses
            # which is from start + 1 to i - 1
            result.append(s[start + 1:i])
            # Set the start for the next primitive component
            start = i + 1
            
    return "".join(result)

# Example usage:
if __name__ == "__main__":
    s1 = "((()))"
    ans1 = removeOuterParentheses(s1)
    print(f'Input: "{s1}", Result: "{ans1}"')

    s2 = "()()"
    ans2 = removeOuterParentheses(s2)
    print(f'Input: "{s2}", Result: "{ans2}"')