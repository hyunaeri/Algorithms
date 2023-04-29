# 백준 17142 연구소 3
import sys
from collections import deque
from itertools import combinations
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
virus = []
answer = int(1e9)

def BFS():
    visited = [ [-1]*N for _ in range(N) ]
    # 최소 시간
    time = 0

    for x, y in queue:
        visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 빈 칸이며 미 방문 상태
                if lab[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                    time = max(time, visited[nx][ny])

                # 비 활성 바이러스를 만남
                # 원래 바이러스가 있던 걸 활성화 시키는 것이므로 시간에는 반영이 안됨.
                elif lab[nx][ny] == 2 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                    

    # BFS가 끝난 이후 바이러스에 감염되지 않은 빈칸이 존재하는 경우
    for i in range(N):
        for j in range(N):
            # 벽이 아닌데 미 방문인 칸이 있는 경우 = 바이러스에 감염되지 않은 칸이 있다
            if lab[i][j] != 1 and visited[i][j] == -1:
                return int(1e9)
            
    return time

# 연구소의 크기, 놓을 수 있는 바이러스의 수
N,M = map(int,read().split())
lab = [ list(map(int, read().rstrip().split())) for _ in range(N) ]

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append([i,j])

for virus_list in combinations(virus,M):
    queue = deque()
    for virus_x, virus_y in virus_list:
        queue.append([virus_x, virus_y])
    answer = min(BFS(), answer)

if answer == int(1e9):
    print(-1)
else:
    print(answer)