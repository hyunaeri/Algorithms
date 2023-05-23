# 백준 1926 그림
import sys
from collections import deque
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 도화지의 세로, 가로
n,m = map(int,read().split())
paper = [ list(map(int,read().split())) for _ in range(n) ]
visited = [ [False]*m for _ in range(n) ]

def bfs(x,y):
    # 초기 넓이는 1
    area = 1

    q = deque()
    q.append([x,y])
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if paper[nx][ny] == 1 and not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny] = True
                    area += 1

    return area

# 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
answer = [0]

for i in range(n):
    for j in range(m):
        # 그림을 찾으면 탐색 시작
        if paper[i][j] == 1 and not visited[i][j]:
            answer.append(bfs(i,j))

print(len(answer) - 1)
print(max(answer))