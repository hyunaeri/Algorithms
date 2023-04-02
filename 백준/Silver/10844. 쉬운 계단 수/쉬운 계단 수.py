# 백준 10844 쉬운 계단 수

import sys

input = sys.stdin.readline
n = int(input())

# dp[n][i] : 길이가 n이고, 마지막 자리의 숫자가 i
dp = [[0 for _ in range(10)] for _ in range(n+1)]
for i in range(1,10):
    dp[1][i] = 1

for i in range(2, n+1):
    # 마지막 자리의 숫자가 0이거나 9이면 예외처리를 해주어야 됨
    # 길이가 i인 마지막 자리의 숫자가 0인 것의 개수는, 길이가 i-1이면서 마지막 자리의 숫자가 1인 것의 개수와 같다 
    dp[i][0] = dp[i-1][1]
    # 길이가 i인 마지막 자리의 숫자가 9인 것의 개수는, 길이가 i-1이면서 마지막 자리의 숫자가 8인 것의 개수와 같다 
    dp[i][9] = dp[i-1][8] 

    # 그 이외의 경우들은 길이가 i-1이면서 마지막 자리의 숫자가 j-1, j+1 인 것들의 합과 같다
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


print(sum(dp[n]) % 1000000000)
