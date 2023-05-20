# 백준 17086 아기 상어 2
import sys
from collections import deque
read = sys.stdin.readline
dx = [-1,1,0,0,-1,1,1,-1]
dy = [0,0,-1,1,-1,1,-1,1]

# N*M 크기의 공간
N, M = map(int,read().split())
space = [ list(map(int,read().split())) for _ in range(N) ]
visited = [ [0]*M for _ in range(N) ]
q = deque()

# 초기 아기상어 위치를 큐에 담음.
for i in range(N):
    for j in range(M):
        if space[i][j] == 1:
            q.append([i,j])


def bfs():
    while q:
        x,y = q.popleft()

        for i in range(8):
            nx,ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 미방문인 빈칸이라면
                if visited[nx][ny] == 0 and space[nx][ny] == 0:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1

                # # 빈칸이고, 방문한 곳
                # elif visited[nx][ny] != 0 and space[nx][ny] == 0:
                #     q.append([nx,ny])
                #     visited[nx][ny] = min(visited[nx][ny],visited[x][y] + 1)

bfs()
# print(visited)
answer = 0
for v in visited:
    answer = max(answer, max(v))

print(answer)