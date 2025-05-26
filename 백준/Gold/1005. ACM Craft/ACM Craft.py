# 백준 1005 ACM Craft
# 위상 정렬
import sys
from collections import deque
read = sys.stdin.readline

def topology_sort(goal):
    queue = deque()

    # 진입 차수가 0인 모든 노드를 큐에 삽입
    for i in range(1, a+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = struct_time[i]

    while queue:
        current = queue.popleft()

        if current == goal:
            return dp[current]

        # 해당 노드와 연결된 모든 노드들의 진입차수 1 빼기
        for next in building[current]:
            indegree[next] -= 1
            dp[next] = max(dp[next], dp[current] + struct_time[next])

            if indegree[next] == 0:
                queue.append(next)


# 테스트 케이스 수
T = int(read())

for _ in range(T):
    # 건물의 수, 건물 간의 건설 순서 규칙 개수
    a, b = map(int,read().split())
    building = [ [] for _ in range(a+1) ]
    indegree = [0] * (a+1)
    struct_time = [-1] + list(map(int,read().split()))

    # 해당 건물을 짓는데 걸리는 최소 시간
    dp = [0] * (a+1)

    # 건설 규칙 저장
    for _ in range(b):
        x, y = map(int, read().split())
        building[x].append(y)

        # y 건물의 진입차수 1 증가
        indegree[y] += 1

    # 승리를 위해 지어야 할 건물
    victory = int(read())
    print(topology_sort(victory))
    # print(dp)