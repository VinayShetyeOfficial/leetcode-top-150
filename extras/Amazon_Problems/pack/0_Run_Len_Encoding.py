# Amazon Video - Run Length Encoding

def runLengthEncoding(s: str) -> str:
    # Edge Case
    if not s: return ''
    
    s = s + '.'
    result = ''
    count = 0
    prev_char = s[0]

    for current_char in s:
        if current_char != prev_char:
            result += str(count) + prev_char
            count = 1
        else:
            count += 1
        prev_char = current_char
        
    return result

    
if __name__ == '__main__':
    s = 'aaaabbbcc'
    ans = runLengthEncoding(s)
    print(f'Encoded String: {ans}')   # Output: Encoded String: 4a3b2c
