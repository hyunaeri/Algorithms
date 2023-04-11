# 백준 2206 벽 부수고 이동하기
# BFS
import sys
from collections import deque
read = sys.stdin.readline

# 세로, 가로
N,M = map(int, read().split())
matrix = [ list(map(int,read().rstrip())) for _ in range(N) ]

# 3차원 배열로 선언 후 벽 파괴 여부를 확인함.
# visited[x][y][0] : 벽 파괴 1회 이후이므로 불가능, [x][y][1] : 벽 파괴 가능
visited = [ [[0]*2 for _ in range(M)] for _ in range(N) ]

# 좌표 값, 벽을 부술 수 있는 횟수
def bfs(x,y,wall_break_left):
    queue = deque()
    queue.append((x,y,wall_break_left))
    # 방문 여부
    visited[x][y][wall_break_left] = 1

    while queue:
        x,y,wall_break_left = queue.popleft()

        # 도착!
        if x == N-1 and y == M-1 :
            return visited[x][y][wall_break_left]

        # 상하좌우
        for dx, dy in [ (-1,0), (1,0), (0,-1), (0,1) ]:
            nx , ny = x + dx, y + dy

            # 그래프의 범위를 벗어나면
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue

            # 벽이 없고, 미 방문 지역이라면
            if matrix[nx][ny] == 0 and visited[nx][ny][wall_break_left] == 0:
                queue.append((nx,ny,wall_break_left))
                visited[nx][ny][wall_break_left] = visited[x][y][wall_break_left] + 1

            # 벽을 만났는데, 아직 벽을 한번도 파괴하지 않았다면 벽을 부수고 지나감
            if matrix[nx][ny] == 1 and wall_break_left == 1:
                queue.append((nx,ny,wall_break_left - 1))
                visited[nx][ny][wall_break_left - 1] = visited[x][y][wall_break_left] + 1
    
    return -1

print(bfs(0,0,1))