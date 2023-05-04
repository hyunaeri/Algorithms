# 백준 14442 벽 부수고 이동하기 2
import sys
from collections import deque
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 행렬의 세로, 가로, 벽을 K개 까지 부숴도 됨
N,M,K = map(int, read().split())
matrix = [ list(map(int,read().rstrip())) for _ in range(N) ]
visited = [ [ [0]*M for _ in range(N) ] for _ in range(K+1) ]

def bfs(break_cnt,x,y):
    q = deque()
    q.append([break_cnt, x, y])
    visited[break_cnt][x][y] = 1

    while q:
        cnt, x, y= q.popleft()

        # 출구 도착!
        if x == N-1 and y == M-1:
            return visited[cnt][x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 빈 칸이라면 평소대로 지나가고
                if matrix[nx][ny] == 0 and visited[cnt][nx][ny] == 0:
                    visited[cnt][nx][ny] = visited[cnt][x][y] + 1
                    q.append([cnt,nx,ny])

                # 아직 벽을 부술 수 있는 카운트가 남아있고, 이전에 내가 벽을 뚫고 가보았는지 확인.
                elif matrix[nx][ny] == 1 and cnt < K and visited[cnt + 1][nx][ny] == 0:
                    # 벽을 부수고 지나간다
                    visited[cnt+1][nx][ny] = visited[cnt][x][y] + 1
                    q.append([cnt+1,nx,ny])

    return -1
    
print(bfs(0,0,0))