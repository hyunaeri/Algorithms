# 2025.05.12 (월)
# 백준 2606 바이러스
# 실버 3

import sys
read = sys.stdin.readline

# 컴퓨터의 수, 연결된 컴퓨터 쌍의 수
N = int(read())
M = int(read())

network = [ [] for _ in range(N + 1) ]
visited = [ False for _ in range(N + 1) ]
answer = 0

for _ in range(M):
  a, b = map(int, read().split())
  network[a].append(b)
  network[b].append(a)
  

def dfs(start):
  global answer
  
  visited[start] = True
  
  for next_node in network[start]:
    if not visited[next_node]:
      dfs(next_node)
      answer += 1

dfs(1)
print(answer)