# 2025.05.13 (화)
# 백준 14226 이모티콘
# 골드 4

from collections import deque
import sys
read = sys.stdin.readline

# 만들어야할 이모티콘 개수
S = int(read())

def bfs():
  visited = [ [False] * (S+1) for _ in range(S+1) ]
  
  # 화면의 이모티콘 개수, 클립보드에 저장된 이모티콘 개수, 걸린 시간 
  q = deque([(1, 0, 0)])
  visited[1][0] = True
  
  while q:
    window, clipboard, time = q.popleft()
    
    if window == S:
      return time
    
    # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
    nw, nc, nt = window, window, time + 1
    
    if not visited[nw][nc]:
      q.append((nw, nc, nt))
      visited[nw][nc] = True
    
    # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 (비어있는 상태에서는 불가능)
    if clipboard > 0:
      nw, nc, nt = window + clipboard, clipboard, time + 1
      
      if 0 <= nw <= S and not visited[nw][nc]:
        q.append((nw, nc, nt))
        visited[nw][nc] = True
    
    # 화면에 있는 이모티콘 중 하나 삭제
    if window > 0:
      nw, nc, nt = window - 1, clipboard, time + 1
      
      if not visited[nw][nc]:
        q.append((nw, nc, nt))
        visited[nw][nc] = True

print(bfs())