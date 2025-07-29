# Climbing Stairs
# https://takeuforward.org/plus/dsa/problems/climbing-stairs

def climbStairs(n):
    # Edge Case
    if n <= 1: return 1
    
    prevStep = 1  # Ways to reach step 0
    curStep = 1   # Ways to reach step 1
    
    for _ in range(2, n + 1):
        nextStep = prevStep + curStep
        prevStep = curStep
        curStep = nextStep
        
    return curStep

if __name__ == '__main__':
    test_cases = [0, 1, 2, 3, 4, 5, 10, 20, 30, 35]

    for n in test_cases:
        ans = climbStairs(n)
        print(f'Ways to climb {n} steps: {ans}')
