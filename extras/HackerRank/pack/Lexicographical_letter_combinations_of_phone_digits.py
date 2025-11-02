# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/lexicographical-letter-combinations-phone-digits

from itertools import product

def minTasksToCancelForNoConflict(digits: str):
    if not digits:
        return []
        
    mp = {
        '0': '0',
        '1': '1',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    pools = [mp[d] for d in digits]
    combos = [''.join(t) for t in product(*pools)]
    print(list(product(*pools)))
    combos.sort()
    return combos
    
print(minTasksToCancelForNoConflict('23'))



# Understanding Product
from itertools import product

listA = ['abc', 'def'] 

print(list(product(*listA)))