# 백준 1261 알고 스팟
# 0-1 BFS
# 벽을 부수고 지나가는 경우는 가중치가 1

import sys
from collections import deque
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 가로, 세로
N,M = map(int, read().split())

# 0: 빈 방, 1: 벽
maze = [ list(map(int,read().rstrip())) for _ in range(M) ]
visited = [ [False]*N for _ in range(M) ]

def bfs(x,y,cnt):
    queue = deque()
    queue.append([x,y,cnt])
    visited[x][y] = True

    while queue:
        x, y, cnt = queue.popleft()
        if x == M-1 and y == N-1:
            print(cnt)
            break

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if 0<=nx<M and 0<=ny<N:
                if maze[nx][ny] == 0 and not visited[nx][ny]:
                    queue.appendleft([nx,ny,cnt])
                    visited[nx][ny] = True

                elif maze[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append([nx,ny,cnt+1])
                    visited[nx][ny] = True

bfs(0,0,0)

