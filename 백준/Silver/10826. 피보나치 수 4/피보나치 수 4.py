# 백준 10826 피보나치 수 4
import sys
read = sys.stdin.readline

n = int(read())
dp = [0] * (10001)
dp[1] = 1
dp[2] = 1

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])