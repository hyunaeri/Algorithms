import sys
read = sys.stdin.readline

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

space = [[] for _ in range(4)]
answer = 0

for i in range(4):
    input_data = list(map(int, read().split()))
    row = []
    for j in range(4):
        row.append([input_data[j * 2], input_data[j * 2 + 1] - 1])
    space[i] = row

def dfs(x, y, score, space):
    global answer
    
    # 상어가 있는 칸의 물고기 방향
    shark_dir = space[x][y][1]

    # 상어가 물고기를 먹음
    score += space[x][y][0]
    answer = max(answer, score)
    space[x][y][0] = 0

    # 물고기 이동
    for i in range(1, 17):
        fx, fy = -1, -1
        found = False
        for a in range(4):
            for b in range(4):
                if space[a][b][0] == i:
                    fx, fy = a, b
                    found = True
                    break
            if found:
                break
        
        # 공간을 모두 돌아도 물고기를 찾지 못한 경우
        if fx == -1 and fy == -1:
            continue

        fd = space[fx][fy][1]
        for j in range(8):
            # 반시계 45도 회전
            nd = (fd + j) % 8 
            nx = fx + dx[nd]
            ny = fy + dy[nd]
            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == x and ny == y):
                space[fx][fy][1] = nd
                space[fx][fy], space[nx][ny] = space[nx][ny], space[fx][fy]
                break

    # 상어 이동 (최대 3칸)
    for step in range(1, 4):
        nx = x + dx[shark_dir] * step
        ny = y + dy[shark_dir] * step
        if 0 <= nx < 4 and 0 <= ny < 4 and space[nx][ny][0] > 0:
            remember_space = [ [ cell[:] for cell in row ] for row in space ]
            dfs(nx, ny, score, remember_space)

dfs(0, 0, 0, space)
print(answer)