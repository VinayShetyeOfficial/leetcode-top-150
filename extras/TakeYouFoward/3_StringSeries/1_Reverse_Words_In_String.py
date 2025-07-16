# Reverse words in a given string / Palindrome Check

def reverseWords(s: str) -> str:
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
     
if __name__ == '__main__':
    s = "welcome to the jungle"
    ans = reverseWords(s)
    print(f'Reversed words in String: {ans}')