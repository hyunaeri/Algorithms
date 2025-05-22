# 2025.05.22 (목)
# 백준 14889 스타트와 링크
# 실버 1

import sys
read = sys.stdin.readline

N = int(read())
stat = [ list(map(int, read().split())) for _ in range(N) ]
visited = [False] * (N)

answer = float('inf')

def get_team_stat(team):
  total_stat = 0
  
  for i in range(len(team)):
    for j in range(i + 1, len(team)):
      a, b = team[i], team[j]
      total_stat += stat[a][b] + stat[b][a]
      
  return total_stat

def backtracking(idx, count):
  global answer
  
  if count == N // 2:
    start_team = [i for i in range(N) if visited[i]]
    link_team = [i for i in range(N) if not visited[i]]
    start_score = get_team_stat(start_team)
    link_score = get_team_stat(link_team)
    answer = min(answer, abs(start_score - link_score))
    return
  
  for num in range(idx, N):
    if not visited[num]:
      visited[num] = True
      backtracking(num + 1, count + 1)
      visited[num] = False
    
backtracking(0, 0)

print(answer)