# 백준 1158 요세푸스 문제
import sys
from collections import deque
read = sys.stdin.readline

N,K = map(int,read().split())
humans = deque([i for i in range(1,N+1)])

result = []

# idx = 0

# for _ in range(N):
#     # 인덱스는 0부터 시작
#     idx += K-1

#     if idx >= len(humans):
#         idx %= len(humans)

#     result.append(str(humans.pop(idx)))

# print("<", ", ".join(result), ">", sep = '')

while humans:
    for _ in range(K-1):
        humans.append(humans.popleft())
    result.append(humans.popleft())

print('<', end = '')
print(*result, sep = ', ', end = '')
print('>')
