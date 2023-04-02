# 백준 11053 가장 긴 증가하는 수열(Longest Increasing Subsequence)
import sys
read = sys.stdin.readline

n = int(read().rstrip())
a = list(map(int,read().rstrip().split()))

# n[i]를 마지막 값으로 가지는 가장 긴 증가부분수열의 길이를 담아 놓을 리스트
LIS = [ 1 for _ in range(n) ]

for i in range(1,n):
    for j in range(i):
        if a[i] > a[j]:
            LIS[i] = max(LIS[i], LIS[j]+1)


# 역 추적 시작
# 가장 작은 것부터 추적하면 안 되는 이유는 
# 만약 5 4 3 2 1 2 3 라는 숫자를 입력받았을 경우 dp는 1 1 1 1 1 2 3 이 된다.
# 즉, 답이 5 2 3 으로 출력될 수도 있다는 얘기이다.

list = []
result = max(LIS)

for i in range(n-1,-1,-1): # 거꾸로 탐색 하면서
    if LIS[i] == result:
        list.append(a[i])
        result -= 1

list.reverse()
print(max(LIS))
print(*list,sep=' ')        
