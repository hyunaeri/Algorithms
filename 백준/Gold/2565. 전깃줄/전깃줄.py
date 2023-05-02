# 백준 2565 전깃줄
import sys
read = sys.stdin.readline

# 두 전봇대 사이의 전깃줄 개수
n = int(read())
electric = []
dp = [1] * n

for _ in range(n):
    x,y = map(int,read().split())
    electric.append([x,y])

electric.sort()

for i in range(1,n):
    for j in range(i):
        if electric[j][1] < electric[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))