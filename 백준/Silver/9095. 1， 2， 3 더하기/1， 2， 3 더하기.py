# 백준 9095 1,2,3 더하기

import sys

input = sys.stdin.readline
T = int(input())
dp_table = [0 for _ in range(11)]
dp_table[1], dp_table[2], dp_table[3] = 1, 2, 4

for _ in range(T):
    n = int(input())
    if n >= 4:
        for i in range(4, n+1):
            dp_table[i] = dp_table[i-1] + dp_table[i-2] + dp_table[i-3]
            
    print(dp_table[n])