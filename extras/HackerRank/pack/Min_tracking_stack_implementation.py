# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/min-tracking-stack/

def processCouponStackOperations(operations):
    stack = []
    minStack = []
    results = []

    for item in operations:
        parts = item.split()
        operation = parts[0]
        number = int(parts[1]) if len(parts) > 1 else None

        if operation == 'push':
            stack.append(number)
            minVal = min(number, minStack[-1] if minStack else number)
            minStack.append(minVal)

        elif operation == 'pop':
            if stack:
                stack.pop()
                minStack.pop()

        elif operation == 'top':
            if stack:
                results.append(stack[-1])
            else:
                results.append(None)

        elif operation == 'getMin':
            if minStack:
                results.append(minStack[-1])
            else:
                results.append(None)

    return results