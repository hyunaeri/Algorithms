# 2025.05.06 (화)
# 백준 1107 리모컨
# 골드 4

import sys
read = sys.stdin.readline

# 목표 채널, 고장난 버튼 개수
target = int(read())
wrong_cnt = int(read())

# 고장난 버튼 리스트
if wrong_cnt == 0: broken = []
else: broken = list(map(int, read().split()))

# 초기 채널 100에서 목표 채널까지 가는 경우
answer = abs(target - 100)

for i in range(1000001):
  num, cnt = str(i), 0
  
  for n in num:
    if int(n) not in broken:
      cnt += 1
    else:
      break
  
  if cnt == len(num):
    answer = min(answer, abs(i - target) + len(str(i)))

print(answer)