# Link: https://takeuforward.org/plus/dsa/problems/count-good-numbers

# Count good Numbers

def count_good_numbers(n: int) -> int:
    MOD = 10**9 + 7
    
    even_positions = (n + 1) // 2  # positions: 0, 2, 4,...
    odd_positions = n // 2         # positions: 1, 3, 5,...

    return (pow(5, even_positions, MOD) * pow(4, odd_positions, MOD)) % MOD
    
    
if __name__ == '__main__':
    n = 50
    ans = count_good_numbers(n)
    print(f'Length of count of good digits: {ans}')


"""
Time Complexity: O(log n) 
- due to modular exponentiation (pow with mod).
Space Complexity: O(1) 
- only a few variables used, no extra space.
"""
