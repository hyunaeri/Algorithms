# 백준 11051 이항계수 2
# 이항계수는 nCr과 같음
import sys
read = sys.stdin.readline

n,k = map(int,read().rstrip().split())

# dp[i]: factorial[i] 와 같음, 메모이제이션
dp = [0 for _ in range(1001)]
dp[0], dp[1], dp[2] = 1, 1, 2

for i in range(3,1001):
    dp[i] = i * dp[i-1]

print( dp[n] // (dp[n-k]*dp[k]) % 10007 )

