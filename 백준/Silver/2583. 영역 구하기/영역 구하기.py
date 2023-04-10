# 백준 2583 영역 구하기
import sys
sys.setrecursionlimit(10001)
read = sys.stdin.readline

# 세로, 가로 길이, 직사각형 개수
M,N,K = map(int, read().rstrip().split())
paper = [ [0]*N for _ in range(M) ]
# print(paper)

for _ in range(K):
    # 왼쪽 아래 꼭짓점의 좌표, 오른쪽 위 꼭짓점의 좌표
    x1,y1,x2,y2 = map(int, read().rstrip().split())

    # 직사각형 영역 만큼 색칠 : 1
    for x in range(y1,y2):
        for y in range(x1,x2):
            if paper[x][y] == 0:
                paper[x][y] = 1

# print(paper)

# DFS
def dfs(x,y):
    global count
    count += 1
    paper[x][y] = 1

    for dx,dy in [ (-1,0),(1,0),(0,-1),(0,1) ]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < M and 0 <= ny < N and paper[nx][ny] == 0:
            dfs(nx,ny)

result = []
for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            count = 0
            dfs(i,j)
            result.append(count)

result.sort()
print(len(result))
print(*result, sep = ' ')