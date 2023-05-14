# 백준 2631 줄 세우기
# LIS 응용
import sys
read = sys.stdin.readline

# 아이들의 수
N = int(read())
child = [int(read()) for _ in range(N)]
dp = [1] * (N)

# 가장 긴 증가하는 부분 수열 구하기
for i in range(1, N):
    for j in range(i):
        if child[i] > child[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_LIS = max(dp)

print(N - max_LIS)