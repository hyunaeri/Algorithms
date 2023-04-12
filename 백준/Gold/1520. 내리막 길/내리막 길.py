# 백준 1520 내리막길
import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

# 세로, 가로의 길이
M,N = map(int,read().rstrip().split())
map = [ list(map(int,read().rstrip().split())) for _ in range(M) ]

# -1 : 미방문
# 0 : 방문
# n : 해당 경로를 통해 도착점까지 갈 수 있는 n가지의 경로가 있음
visited = [ [-1]*N for _ in range(M) ]

def dfs(x,y):
    if x == M-1 and y == N-1:
        return 1
    
    # 이미 방문한적이 있다면
    if visited[x][y] != -1:
        return visited[x][y]
    
    visited[x][y] = 0

    for dx, dy in [ (-1,0),(1,0),(0,-1),(0,1) ]:
        nx,ny = x + dx, y + dy

        # 그래프의 범위를 벗어나면,
        if nx < 0 or ny < 0 or nx >= M or ny >= N:
            continue
        
        # 범위 안이면서, 내리막길일 경우에만
        if map[nx][ny] < map[x][y]:
            visited[x][y] += dfs(nx,ny)

    return visited[x][y]

print(dfs(0,0))