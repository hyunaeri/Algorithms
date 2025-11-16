# 백준 17070
# 골드 5
# https://www.acmicpc.net/problem/17070

import sys
read = sys.stdin.readline

# dir (0: 가로, 1: 세로, 2: 대각선)
def dfs(x, y, dir):
  global N, answer, house_info
  
  # 목표 지점 도달
  if x == (N - 1) and y == (N - 1):
    answer += 1
    return
  
  # 가로
  if dir == 0:
    # 회전 없이
    if 0 <= x < N and 0 <= y + 1 < N and house_info[x][y + 1] == 0:
      dfs(x, y + 1, 0)
    
    # 45도 회전 (3방향 체크), 대각선으로 전환
    if 0 <= x + 1 < N and 0 <= y + 1 < N and house_info[x][y + 1] == 0 and house_info[x + 1][y + 1] == 0 and house_info[x + 1][y] == 0:
      dfs(x + 1, y + 1, 2)
  
  # 세로
  if dir == 1:
    # 회전 없이
    if 0 <= x + 1 < N and 0 <= y < N and house_info[x + 1][y] == 0:
      dfs(x + 1, y, 1)
      
    # 45도 회전 (3방향 체크), 대각선으로 전환
    if 0 <= x + 1 < N and 0 <= y + 1 < N and house_info[x][y + 1] == 0 and house_info[x + 1][y + 1] == 0 and house_info[x + 1][y] == 0:
      dfs(x + 1, y + 1, 2)
  
  # 대각선
  if dir == 2:
    # 회전 없이 대각선 유지
    if 0 <= x + 1 < N and 0 <= y + 1 < N and house_info[x][y + 1] == 0 and house_info[x + 1][y + 1] == 0 and house_info[x + 1][y] == 0:
      dfs(x + 1, y + 1, 2)
    
    # 45도 회전, 가로
    if 0 <= x < N and 0 <= y + 1 < N and house_info[x][y + 1] == 0:
      dfs(x, y + 1, 0)
    
    # 45도 회전, 세로
    if 0 <= x + 1 < N and 0 <= y < N and house_info[x + 1][y] == 0:
      dfs(x + 1, y, 1)


if __name__ == '__main__':
  answer = 0
  
  # 집의 크기 N * N
  N = int(read())
  
  # 집의 상태 (0 : 빈칸, 1 : 벽)
  house_info = [ list(map(int, read().rstrip().split())) for _ in range(N) ]
  
  dfs(0, 1, 0)
  
  print(answer)