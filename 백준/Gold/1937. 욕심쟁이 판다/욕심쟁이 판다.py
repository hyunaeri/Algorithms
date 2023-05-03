import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(read())
forest = [ list(map(int,read().rstrip().split())) for _ in range((n)) ]

# dp[i][j] : 판다를 (i,j)에 처음 내려놓았을 때 이동할 수 있는 최대 칸
dp = [ [0]*n for _ in range(n) ]

def dfs(x,y):
    # 한번 방문한 칸은 그대로 리턴
    if dp[x][y]:
        return dp[x][y]

    # 처음 방문한 칸은 무조건 먹을 수 있음
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if forest[nx][ny] > forest[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx,ny) + 1)

    return dp[x][y]

for i in range(n):
    for j in range(n):
        dfs(i,j)

result = 0
for values in dp:
    result = max(result, max(values))

print(result)