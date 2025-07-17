# Pow(x,n)

def myPow(x: int, n: int):
    def helper(x, n):
        if x == 0: return 0
        if n == 0: return 1
        
        res = helper(x, n // 2)
        res = res * res
        return x * res if n % 2 else res
    
    res = helper(x, abs(n))
    return res if n >= 0 else 1 / res
    
    
if __name__ == '__main__':
    x = 2.0000
    n = 10
    ans = myPow(x, n)
    print(f'{x} ^ {n}: {ans}')