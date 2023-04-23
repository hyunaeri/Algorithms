# 백준 2133 타일 채우기
import sys
read = sys.stdin.readline

n = int(read())
dp = [0] * (31)
dp[2] = 3

for i in range(4,n+1):
    if i % 2 == 1:
        dp[i] = 0
    else:
        dp[i] = 2 + (3 * dp[i-2]) + (2 * sum(dp[:i-3]))

print(dp[n])