# 백준 1931 회의실 배정
# 회의가 끝나는 시간을 기준으로 정렬하고
# 끝나는 시간이 같다면 시작하는 시간이 빠른 것 기준으로 정렬

import sys
read = sys.stdin.readline

# 회의의 수
n = int(read())
meeting = [list(map(int,read().split())) for _ in range(n)]
meeting = sorted(meeting, key=lambda x: (x[1], x[0]) )

dp = [[0,0]]
for i in range(n):
    # 시작하는 시간이 끝나는 시간보다 크면
    if meeting[i][0] >= dp[-1][1]:
        dp.append(meeting[i])

print(len(dp) - 1)
