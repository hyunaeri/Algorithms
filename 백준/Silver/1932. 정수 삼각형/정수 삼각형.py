# 백준 1932 정수 삼각형
import sys
read = sys.stdin.readline

# 삼각형의 크기
n = int(read().rstrip())
tri = [ list(map(int,read().rstrip().split())) for _ in range(n)  ]
# print(tri)

dp = [ [0]*(i+1) for i in range(n) ]
dp[0][0] = tri[0][0]

for i in range(1,n):
    for j in range(len(tri[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]
        elif j == len(tri[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tri[i][j]

print(max(dp[n-1]))