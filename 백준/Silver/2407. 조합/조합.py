# 백준 2407 조합론
import sys
import math
read = sys.stdin.readline

# nCm
n,m = map(int,read().split())
result = math.comb(n,m)
print(result)
