# 백준 14501
# 실버 3
# https://www.acmicpc.net/problem/14501

import sys
read = sys.stdin.readline

# N + 1일에 퇴사
N = int(read())
consult = [ [0,0] ] + [ list(map(int, read().rstrip().split())) for _ in range(N) ]

# dp[i] : 'i' 일차 에 얻을 수 있는 최대 금액
dp = [0] * (N + 2)

for i in range(1, N + 1):
  # 이전 최댓값 반영
  dp[i + 1] = max(dp[i + 1], dp[i])
  
  period, income = consult[i]
  end_day = i + period
  
  if end_day <= N + 1:
    dp[end_day] = max(dp[end_day], dp[i] + income)
  
print(dp[-1])