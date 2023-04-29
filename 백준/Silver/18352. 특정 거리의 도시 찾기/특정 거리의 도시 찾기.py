# 백준 18352 특정 거리의 도시 찾기
import sys
import heapq
read = sys.stdin.readline
INF = int(2e9)

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
v, e, k, start_city = map(int, read().split())
graph = [ [] for _ in range(v+1) ]
distance = [INF] * (v+1)
queue = []

for _ in range(e):
    x, y = map(int,read().split())
    # 모든 도로는 가중치가 1
    graph[x].append([y,1])


def dijkstra(start):
    # 자기 자신으로 가는 비용은 0
    distance[start] = 0
    heapq.heappush(queue, [0, start])

    while queue:
        dist, current_node = heapq.heappop(queue)

        if distance[current_node] < dist:
            continue

        for next_node, next_cost in graph[current_node]:
            cost = dist + next_cost

            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(queue, [cost, next_node])

    return distance

result = dijkstra(start_city)
answer = []

for i in range(1, v+1):
    if result[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    print(*answer, sep = '\n')