# 백준 1138 한 줄로 서기
import sys
read = sys.stdin.readline

# 사람의 수
N = int(read())
height = [-1] + list(map(int,read().split()))
result = [0] * (N)

for i in range(1,N+1):
    # i 키를 가진 사람 왼쪽에 i 보다 큰 tall 명이 있음.
    tall = height[i]
    cnt_zero = 0

    for j in range(N):
        if result[j] == 0:
            if cnt_zero == tall:
                result[j] = i
                break
            cnt_zero += 1

print(*result, sep =' ')