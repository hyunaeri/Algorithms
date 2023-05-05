# 백준 2839 설탕 배달
import sys
read = sys.stdin.readline

N = int(read().rstrip())
dp = [ 10001 for _ in range(N+5) ]
dp[3], dp[5] = 1, 1

for i in range(6, N+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1
    
if dp[N] >= 10001:
    print("-1")
else:
    print(dp[N])