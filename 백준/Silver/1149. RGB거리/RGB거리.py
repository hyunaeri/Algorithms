# 2025.04.08 (화)
# 백준 1149 RGB 거리
# 실버 1

import sys
read = sys.stdin.readline

N = int(read())
house = [ list(map(int, read().split())) for _ in range(N) ]

# 0: R, 1: G, 2: B
dp = [ [0] * 3 for _ in range(N) ]
dp[0][0] = house[0][0]
dp[0][1] = house[0][1]
dp[0][2] = house[0][2]

for i in range(1, N):
  dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + house[i][0]
  dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + house[i][1]
  dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + house[i][2]

answer = min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2])
print(answer)

