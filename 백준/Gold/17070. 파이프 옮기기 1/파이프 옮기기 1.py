# 백준 17070
# 골드 5
# https://www.acmicpc.net/problem/17070

import sys
read = sys.stdin.readline

if __name__ == '__main__':
  
  # 집의 크기 N * N
  N = int(read())
  
  # 집의 상태 (0: 빈칸, 1: 벽)
  house_info = [ list(map(int, read().rstrip().split())) for _ in range(N) ]
  
  # dp[dir][x][y] (0: 가로, 1: 세로, 2: 대각선)
  dp = [ [[0] * N for _ in range(N)] for _ in range(3) ]
  dp[0][0][1] = 1
  
  # 첫 행 가로 방향 DP 테이블 채우기
  for i in range(2, N):
    if house_info[0][i] == 0:
      dp[0][0][i] = dp[0][0][i - 1]
  
  # 나머지 DP 테이블 채우기
  for i in range(1, N):
    for j in range(1, N):
      # 대각선 파이프 놓기
      if house_info[i][j] == 0 and house_info[i][j-1] == 0 and house_info[i-1][j] == 0:
        dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
      
      if house_info[i][j] == 0:
        # 가로 파이프 놓기
        dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
        # 세로 파이프 놓기
        dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
        
  print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])