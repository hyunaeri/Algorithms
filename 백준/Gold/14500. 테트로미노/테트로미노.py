# 2025.05.12 (월)
# 백준 14500 테트로미노
# 골드 4

from collections import deque
import sys
read = sys.stdin.readline

# 종이의 세로, 가로 크기
N, M = map(int, read().split())
paper = [list(map(int, read().split())) for _ in range(N)]

# 일반적인 4칸 연결 도형은 bfs로 탐색
def bfs(x, y):
  max_sum = 0
  q = deque([(x, y, 1, paper[x][y], [(x, y)])])
  
  while q:
    x, y, depth, s, path = q.popleft()
    
    if depth == 4:
      max_sum = max(max_sum, s)
      continue
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx, ny = x + dx, y + dy
      
      if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in path:
        new_path = path + [(nx, ny)]
        q.append((nx, ny, depth + 1, s + paper[nx][ny], new_path))
        
  return max_sum

# 'ㅗ' 모양 같은 경우는 bfs로 탐색할 수 없음
def extra_shape(x, y):
  max_sum = 0
  
  # 중앙 + 3방향으로 표현
  shapes = [
    [(0,0), (-1,0), (0,-1), (0,1)],  # ㅗ
    [(0,0), (1,0), (0,-1), (0,1)],   # ㅜ
    [(0,0), (0,-1), (-1,0), (1,0)],  # ㅓ
    [(0,0), (0,1), (-1,0), (1,0)]    # ㅏ
  ]
  
  for shape in shapes:
    is_valid = True
    s = 0
    
    for dx, dy in shape:
      nx, ny = x + dx, y + dy
      
      if 0 <= nx < N and 0 <= ny < M: 
        s += paper[nx][ny]
      else:
        is_valid = False
        break
    
    if is_valid:
      max_sum = max(max_sum, s)
      
  return max_sum

answer = 0

for i in range(N):
  for j in range(M):
    general = bfs(i, j)
    extra = extra_shape(i, j)
    answer = max(answer, general, extra)

print(answer)