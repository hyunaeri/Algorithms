# 백준 2146 다리 만들기
import sys
from collections import deque
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 지도의 크기
N = int(read())
islands = [ list(map(int,read().rstrip().split())) for _ in range(N) ]
visited = [[False] * N for _ in range(N)]
count = 1
answer = int(2e9)

def divide_island(x,y):
    global count
    queue = deque()
    queue.append([x,y])
    islands[x][y] = count
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if islands[nx][ny] == 1:
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                    islands[nx][ny] = count

def find_min_distance(count):
    global answer
    dist = [ [0]*N for _ in range(N) ]
    q = deque()

    for i in range(N):
        for j in range(N):
            if islands[i][j] == count:
                q.append([i,j])
                
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:

                # 바다를 만났고, 미 방문
                if islands[nx][ny] == 0 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])

                # 육지를 만났는데, 분리된 다른 육지임
                elif islands[nx][ny] > 0 and islands[nx][ny] != count:
                    answer = min(answer, dist[x][y])
                    return

# 육지 분리
for i in range(N):
    for j in range(N):
        if islands[i][j] == 1 and not visited[i][j]:
            divide_island(i,j)
            count += 1

for i in range(1, count):
    find_min_distance(i)

print(answer)
