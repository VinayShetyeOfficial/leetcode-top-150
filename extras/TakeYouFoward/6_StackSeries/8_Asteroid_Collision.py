# Asteroid Collision

def asteroidCollision(asteroids):
    stack = []

    for asteroid in asteroids:
        while stack and stack[-1] > 0 and asteroid < 0:
            top = stack[-1]
            if abs(top) == abs(asteroid):
                stack.pop()
                break
            elif abs(top) > abs(asteroid):
                break
            else:
                stack.pop()
                continue
        else:
            stack.append(asteroid)

    return stack

# ----------- Test Driver Code -----------
if __name__ == '__main__':
    test_cases = [
        [2, -2],               # []
        [10, 2, -5],           # [10]
        [1, -2, -2, -2],       # [-2, -2, -2]
        [8, -8],               # []
        [5, 10, -5],           # [5, 10]
        [-2, -1, 1, 2],        # [-2, -1, 1, 2]
        [1, 2, 3, -3, -2, -1], # []
    ]

    for asteroids in test_cases:
        ans = asteroidCollision(asteroids)
        print(f'Asteroids: {asteroids} -> Result: {ans}')
