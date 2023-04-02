# 백준 1010 다리 놓기
from itertools import combinations
import sys
read= sys.stdin.readline

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)


T= int(read())
for _ in range(T):
    n,m = map(int, read().rstrip().split())
    print(factorial(m) // (factorial(m-n) * factorial(n)))