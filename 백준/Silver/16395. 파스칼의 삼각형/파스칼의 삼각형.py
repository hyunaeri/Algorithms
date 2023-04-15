# 백준 16395 파스칼의 삼각형
import sys
read = sys.stdin.readline

n,k = map(int,read().split())
pascal = [ [0]*(i+1) for i in range(n+1) ]
pascal[1][1] = 1

for i in range(2,n+1):
    for j in range(1,i+1):
        if j == 1 or j == i:
            pascal[i][j] = 1
        else:
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

print(pascal[n][k])