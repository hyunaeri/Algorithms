# 백준 9466 텀 프로젝트
import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

# Test case
T = int(read())

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    student = students[x]

    # 다음 학생이 이미 방문처리가 되어있다면
    if visited[student]:
        if student in cycle:
            # 사이클을 이루는 학생들만 팀을 이룸
            result += cycle[cycle.index(student):]
            return
    else:
        dfs(student)

for _ in range(T):
    # the number of students
    n = int(read())
    students = [0] + (list(map(int,read().split())))
    visited = [True] + [False] * (n)
    result = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(result))