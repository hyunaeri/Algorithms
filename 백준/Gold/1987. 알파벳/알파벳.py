# 백준 1987 알파벳
# DFS
import sys
# sys.setrecursionlimit(10**6)
read = sys.stdin.readline

# 세로, 가로
R,C = map(int, read().rstrip().split())
board = [ list(map(str,read().rstrip())) for _ in range(R) ]
visited = set()
ans = 0

def DFS(x,y,count):
    global ans
    # 세트에 추가
    visited.add(board[x][y])
    ans = max(ans, count)

    # 상하좌우
    for dx,dy in [ (-1,0),(1,0),(0,-1),(0,1) ]:
        nx = x + dx
        ny = y + dy

        # 그래프의 범위를 벗어나지 않을 경우
        if 0 <= nx < R and 0 <= ny < C:
            # 방문하지 않은 경우
            if not board[nx][ny] in visited:
                DFS(nx,ny,count+1)

    visited.remove(board[x][y])
        
DFS(0,0,1)
print(ans)