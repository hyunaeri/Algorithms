# 백준 2056 작업
import sys
from collections import deque
read = sys.stdin.readline

def topology_sort():
    queue = deque()

    # 진입 차수가 0인 노드들을 모두 큐에 넣음
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = time[i]

    while queue:
        current = queue.popleft()

        # 현재 노드와 연결되어 있는 모든 노드의 진입 차수 1 감소
        for next in task[current]:
            indegree[next] -= 1
            dp[next] = max(dp[next], dp[current] + time[next])

            if indegree[next] == 0:
                queue.append(next)

    return max(dp)        


# 수행 해야 할 작업의 수, 각각의 작업마다 걸리는 시간
N = int(read())
task = [ [] for _ in range(N+1) ]
indegree = [0] * (N+1)
time = [0] * (N+1)

# 해당 작업을 하는데 걸리는 최소 시간
dp = [0] * (N+1)

for i in range(1, N+1):
    info = list(map(int,read().split()))

    # i번 작업에 걸리는 시간
    time[i] = info[0]
    # i번 작업에 대해 선행 관계에 있는 작업들의 개수(= 진입 차수 개수)
    indegree[i] = info[1]

    if indegree[i] != 0:
        # 선행 관계에 있는 작업들의 번호
        for t in info[2:]:
            task[t].append(i)

answer = topology_sort()
print(answer)