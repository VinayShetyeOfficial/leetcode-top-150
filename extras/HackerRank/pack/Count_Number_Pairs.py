# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-number-pairs

# Optimized
def countAffordablePairs(prices, budget):
    n = len(prices)
    if n < 2:
        return 0

    left, right = 0, n - 1
    count = 0

    while left < right:
        if prices[left] + prices[right] <= budget:
            # All pairs (left, left+1), (left, left+2), ..., (left, right)
            count += (right - left)
            left += 1
        else:
            right -= 1

    return count


# Brute Force O(n)^2
def countAffordablePairs(prices, budget):
    # Write your code here
    count = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[i] + prices[j] <= budget:
                count += 1
                
    return count   