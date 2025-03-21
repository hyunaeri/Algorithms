# 백준 2579번 계단 오르기
import sys
read = sys.stdin.readline

stairCnt = int(read())
stairs = [0] * 301

for i in range(1, stairCnt + 1):
  stairs[i] = int(read())

# dp 테이블 초기화
dp = [0] * 301

dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, stairCnt + 1):
  dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
  
print(dp[stairCnt])