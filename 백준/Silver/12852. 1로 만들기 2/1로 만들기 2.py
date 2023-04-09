# 백준 12852 1로 만들기 2
import sys
read = sys.stdin.readline

N = int(read())
dp = [0] * (1000001)
backtracking = [0] * (1000001)
dp[2] = 1
backtracking[2] = 1

for i in range(3, N+1):
    dp[i] = dp[i-1] + 1
    backtracking[i] = i-1

    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        backtracking[i] = i // 2
    
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        backtracking[i] = i // 3

def back(num):
    print(num, end = ' ')
    while num != 1:
        print(backtracking[num], end = ' ')
        num = backtracking[num]


print(dp[N])
back(N)