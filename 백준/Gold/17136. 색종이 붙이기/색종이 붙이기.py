# 백준 17136
# 골드 2
# https://www.acmicpc.net/problem/17136

import sys
read = sys.stdin.readline

INF = int(1e9)

def check_area(x, y, size):
    global paper

    # 범위 밖으로 나가면 안 됨
    if x + size > 10 or y + size > 10:
        return False

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != 1:
                return False

    return True


def paste(x, y, size, value):
    global paper

    for i in range(x, x + size):
        for j in range(y, y + size):
            paper[i][j] = value


def dfs(pos, used):
    global answer, paper, paper_count

    # 이미 지금까지 쓴 색종이가 최적해보다 많으면 더 볼 필요 없음
    if used >= answer:
        return

    # 끝까지 다 확인했으면(= 모든 1을 가린 상태라면) 답 갱신
    if pos == 100:
        answer = min(answer, used)
        return

    x = pos // 10
    y = pos % 10

    # 현재 칸이 0이면 그냥 다음 칸으로
    if paper[x][y] == 0:
        dfs(pos + 1, used)
        return

    # 큰 색종이부터 시도 (5x5 → 1x1)
    for size in range(5, 0, -1):
        # 해당 크기 색종이 남아 있는지, 붙일 수 있는지 확인
        if paper_count[size] > 0 and check_area(x, y, size):
            # 색종이 붙이기
            paste(x, y, size, 0)
            paper_count[size] -= 1

            dfs(pos + 1, used + 1)

            # 되돌리기 (백트래킹)
            paste(x, y, size, 1)
            paper_count[size] += 1


if __name__ == '__main__':

    # 색종이 개수 (1~5 각 5개씩)
    paper_count = {i: 5 for i in range(1, 6)}

    # 종이 정보
    paper = [list(map(int, read().split())) for _ in range(10)]

    answer = INF
    dfs(0, 0)

    print(answer if answer != INF else -1)
    