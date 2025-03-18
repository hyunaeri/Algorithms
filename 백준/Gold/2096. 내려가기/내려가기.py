# 백준 2096 : 내려가기
import sys
read = sys.stdin.readline

row = int(read())

cur_score = list(map(int, read().split()))

max_dp = cur_score[:]
min_dp = cur_score[:] 

for _ in range(row - 1):
  cur_score = list(map(int, read().split()))
  
  max_dp = [
    max(max_dp[0], max_dp[1]) + cur_score[0], 
    max(max_dp[0], max_dp[1], max_dp[2]) + cur_score[1], 
    max(max_dp[1], max_dp[2]) + cur_score[2]
  ]
  
  min_dp = [
    min(min_dp[0], min_dp[1]) + cur_score[0], 
    min(min_dp[0], min_dp[1], min_dp[2]) + cur_score[1], 
    min(min_dp[1], min_dp[2]) + cur_score[2]
  ]
      
print(max(max_dp), min(min_dp))