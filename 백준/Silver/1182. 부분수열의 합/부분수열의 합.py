import sys
read = sys.stdin.readline

N, S = map(int, read().split())
arr = list(map(int, read().split()))
answer = 0

def backtracking(start, total):
    global answer
    if start == N:
        if total == S:
            answer += 1
        return

    # 현재 원소를 선택하는 경우
    backtracking(start + 1, total + arr[start])
    # 현재 원소를 선택하지 않는 경우
    backtracking(start + 1, total)

backtracking(0, 0)

# 공집합 제외
if S == 0:
    answer -= 1

print(answer)