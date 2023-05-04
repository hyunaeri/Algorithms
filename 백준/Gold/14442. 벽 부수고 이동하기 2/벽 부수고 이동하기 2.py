# 백준 14442 벽 부수고 이동하기 2
import sys
from collections import deque
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 행렬의 세로, 가로, 벽을 K개 까지 부숴도 됨
N,M,K = map(int, read().split())
matrix = [ list(map(int,read().rstrip())) for _ in range(N) ]
visited = [ [ [0]*(K+1) for _ in range(M) ] for _ in range(N) ]

def bfs(x,y,break_cnt):
    q = deque()
    q.append([x,y,break_cnt])
    visited[x][y][break_cnt] = 1

    while q:
        x, y, cnt = q.popleft()

        # 출구 도착!
        if x == N-1 and y == M-1:
            return visited[x][y][cnt]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 빈 칸이라면 평소대로 지나가고
                if matrix[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    q.append([nx,ny,cnt])

                # 아직 벽을 부술 수 있는 카운트가 남아있고, 이전에 내가 벽을 뚫고 가보았는지 확인.
                elif matrix[nx][ny] == 1 and cnt != 0 and visited[nx][ny][cnt - 1] == 0:
                    # 벽을 부수고 지나간다
                    visited[nx][ny][cnt - 1] = visited[x][y][cnt] + 1
                    q.append([nx,ny,cnt - 1])

    return -1
    
print(bfs(0,0,K))