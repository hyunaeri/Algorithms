# 백준 15988 1,2,3 더하기 3
import sys
read = sys.stdin.readline

T = int(read())

dp = [0] * (1000001)
dp[1] = 1
dp[2] = 2
dp[3] = 4
    
for i in range(4, len(dp)):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for _ in range(T):
    n = int(read())
    print(dp[n])


