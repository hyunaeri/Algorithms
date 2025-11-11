# 백준 3190
# 골드 4
# https://www.acmicpc.net/problem/3190

from collections import deque
import sys
read = sys.stdin.readline

def rotate(dir, command):
  if command == 'L' : return (dir - 1) % 4
  else : return (dir + 1) % 4

if __name__ == '__main__':
  
  # 우 하 좌 상
  dirs = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
  
  # 보드의 크기 N * N
  # 0 : 빈칸
  # 1 : 사과
  # 2 : 뱀
  N = int(read())
  board = [ [0] * N for _ in range(N) ]
  
  # 사과의 개수, 정보
  K = int(read())
  for _ in range(K):
    apple_x, apple_y = map(int, read().split())
    board[apple_x - 1][apple_y - 1] = 1
  
  # 뱀의 방향 변환 횟수, 정보
  # 'L' : 반시계 90도
  # 'R' : 시계 90도
  L = int(read())
  change_dir = deque()
  for _ in range(L):
    time, d = read().rstrip().split()
    change_dir.append((int(time), d))
  
  # 뱀이 위치한 모든 좌표가 덱에 저장 (꼬리는 항상 0번 인덱스)
  snake = deque([(0, 0)])
  head_x, head_y = 0, 0
  board[0][0] = 2
  dir_idx = 0
  
  playtime = 0
  
  while True:
    # 1초 증가
    playtime += 1
    dx, dy = dirs[dir_idx]
    nx, ny = head_x + dx, head_y + dy
    
    # 다음 위치가 벽이면 게임 아웃, 다음 위치가 자기 자신의 몸이어도 게임 아웃
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
      break
    
    # 다음 위치가 사과
    if board[nx][ny] == 1:
      board[nx][ny] = 2
    else:
      board[nx][ny] = 2
      tail_x, tail_y = snake.popleft()
      board[tail_x][tail_y] = 0
      
    # 새로운 머리
    snake.append((nx, ny))
    head_x, head_y = nx, ny
    
    # 회전할 시간이면
    if change_dir and playtime == change_dir[0][0]:
      dir_idx = rotate(dir_idx, change_dir[0][1])
      change_dir.popleft()
    
  print(playtime)