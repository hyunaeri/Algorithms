# 백준 1516 게임개발
import sys
from collections import deque
read = sys.stdin.readline

def topology_sort():
    queue = deque()

    # 진입차수가 0인 모든 노드를 큐에 넣음
    for i in range(1,N+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] += times[i]

    while queue:
        current = queue.popleft()

        # 현재 노드와 연결된 모든 노드의 진입차수 감소
        for next in graph[current]:
            indegree[next] -= 1
            dp[next] = max(dp[next], dp[current] + times[next])

            if indegree[next] == 0:
                queue.append(next)

    return dp

# 건물의 종류
N = int(read())
times = [0] * (N+1)
indegree = [0] * (N+1)
graph = [ [] for _ in range(N+1) ]
dp = [0] * (N+1)

for i in range(1, N+1):
    temp = list(map(int,read().split()))

    # 건물을 짓는데 걸리는 시간
    times[i] = temp[0]
    # 입력의 마지막은 -1로 받으니까, 맨 마지막 인덱스를 제외하고
    for x in temp[1:-1]:
        graph[x].append(i)
        indegree[i] += 1

# print(graph)
answer = topology_sort()[1:]
print(*answer, sep = '\n')