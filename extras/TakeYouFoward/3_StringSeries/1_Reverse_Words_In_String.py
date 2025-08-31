# Link: https://takeuforward.org/plus/dsa/problems/reverse-every-word-in-a-string

# Reverse words in a given string

def reverseWords(s: str) -> str:
    words = s.split()          # Split string into words
    reversed_words = words[::-1]  # Reverse the list of words
    return ' '.join(reversed_words)  # Join back into a string
     
if __name__ == '__main__':
    s = "welcome to the jungle"
    ans = reverseWords(s)
    print(f'Reversed words in String: {ans}')

"""
Time Complexity (TC): O(N) -> splitting, reversing, and joining are all O(N)
Space Complexity (SC): O(N) -> storing the words list and reversed_words list
"""
