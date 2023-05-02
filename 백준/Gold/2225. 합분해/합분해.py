# 백준 2235 합분해
import sys
read = sys.stdin.readline

N,K = map(int,read().split())

# dp[N][K] = N을 0~N 수 중 K개로 만들 수 있는 경우의 수
dp = [ [0]*(K+1) for _ in range(N+1) ]

for i in range(K+1):
    dp[0][i] = 1

for i in range(1, N+1):
    dp[i][1] = 1
    for j in range(2, K+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1] % 1000000000)