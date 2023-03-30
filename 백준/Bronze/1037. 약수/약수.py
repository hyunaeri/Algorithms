# 백준 1037 약수
import sys
read = sys.stdin.readline

# 약수의 개수
n = int(read())
div = list(map(int,read().rstrip().split()))
div.sort()

print(div[0]*div[-1])