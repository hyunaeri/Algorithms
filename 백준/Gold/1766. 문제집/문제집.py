# 백준 1766 문제집
# 위상 정렬과 우선순위 큐
import sys
import heapq
read = sys.stdin.readline

def topology_sort():
    queue = []

    # 진입 차수가 0인 모든 노드를 큐에 넣음
    for i in range(1,N+1):
        if indegree[i] == 0:
            # 진입 차수가 동일하게 0이더라도 문제번호가 작은 순서대로 풀어야 하므로, heap 이용
            heapq.heappush(queue,i)

    while queue:
        current = heapq.heappop(queue)
        print(current, end =' ')
        
        for next in graph[current]:
            indegree[next] -= 1
            
            # 현재 노드로 인해 다음 노드의 진입차수가 0이 된 경우 우선순위를 가짐.
            if indegree[next] == 0:
                heapq.heappush(queue,next)

# 문제의 수, 먼저 푸는것이 좋은 문제에 대한 정보의 개수
N,M = map(int,read().split())
indegree = [0] * (N+1)
graph = [ [] for _ in range(N+1) ]

for _ in range(M):
    # a를 b보다 먼저 풀어야 함.
    a,b = map(int,read().split())
    graph[a].append(b)
    indegree[b] += 1

topology_sort()