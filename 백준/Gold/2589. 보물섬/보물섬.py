# 백준 2589 보물섬
import sys
from collections import deque
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 세로, 가로
n,m = map(int,read().split())
island = [ list(map(str,read().rstrip())) for _ in range(n) ]

def bfs(x,y):
    cnt = 0
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if island[nx][ny] == 'L' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                    cnt = max(cnt, visited[nx][ny])

    return cnt

result = 0

for i in range(n):
    for j in range(m):
        if island[i][j] == 'L':
            visited = [ [-1]*m for _ in range(n) ]
            result = max(result, bfs(i,j))

print(result)