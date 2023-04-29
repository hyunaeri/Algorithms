# 백준 17141 연구소 2
from collections import deque
from itertools import combinations
import sys
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
virus_possible = []
answer = int(1e9)

# 연구소의 크기, 놓을 수 있는 바이러스의 개수
N,M = map(int,read().rstrip().split())

# 0: 빈 칸 
# 1: 벽
# 2: 바이러스를 놓을 수 있는 칸
lab = [ list(map(int,read().rstrip().split())) for _ in range(N) ]

def bfs(v):
    queue = deque(v)
    visited = [ [-1]*N for _ in range(N) ]
    # 최소 시간
    time = 0

    # 바이러스들은 방문 초기값 0
    for x,y in queue:
        visited[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                # 미 방문상태인 빈 칸으로 이동한 경우(바이러스를 모두 큐에 담고 시작했기에, 기존의 2도 빈칸으로 간주)
                if visited[nx][ny] == -1 and lab[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                    # 최소 시간 갱신
                    time = max(time, visited[x][y]+1)

    # BFS가 끝난 이후 바이러스에 감염되지 않은 빈칸이 존재하는 경우
    for i in range(N):
        for j in range(N):
            # 벽이 아닌데 미 방문인 칸이 있는 경우
            if lab[i][j] != 1 and visited[i][j] == -1:
                return int(1e9)
            
    return time


for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus_possible.append([i,j])

for v in combinations(virus_possible, M):
    answer = min(bfs(v), answer)

# 모든 경우의 수에 대하여 바이러스를 전부 감염 못시키는 경우는 1e9를 리턴
if answer == int(1e9):
    print(-1)
else:
    print(answer)