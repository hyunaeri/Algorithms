# 백준 7576 토마토
# BFS
from collections import deque
import sys
read = sys.stdin.readline

def BFS():
    while queue:
        x, y = queue.popleft()
        # 상하좌우로는 영향을 주기에..
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x + dx
            ny = y + dy

            # 토마토 칸 범위를 벗어나지않고, 익지 않은 토마토가 존재할 경우
            if 0 <= nx < n and 0 <= ny < m and tomatoes[nx][ny] == 0: 
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append((nx,ny))

# 가로 칸의 수, 세로 칸의 수
m, n = map(int,read().rstrip().split())

# 1: 익은 토마토
# 0: 안 익은 토마토 
# -1: 토마토가 들어있지 않음
tomatoes = [ list(map(int, read().rstrip().split())) for _ in range(n) ]
queue = deque()

# 익은 토마토의 위치를 큐에 저장
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            queue.append((i,j))

BFS()
result = 0
for tomato_line in tomatoes:
    for tomato in tomato_line:
        if tomato == 0:
            print("-1")
            exit()
    result = max(result, max(tomato_line))  

print(result - 1)

