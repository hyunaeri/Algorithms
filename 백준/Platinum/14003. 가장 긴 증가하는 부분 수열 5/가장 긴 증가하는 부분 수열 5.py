# 백준 14003 가장 긴 증가하는 부분 수열 5 (LIS : Longest Increasing Subsequence)
# 기존의 LIS 알고리즘으로 풀기엔 입력의 크기가 너무 큼, 최대 길이가 1,000,000
# 수열을 순회하며 나오는 숫자가 현재까지 만든 LIS 마지막 숫자보다 작다면, 교체해줄 자리를 전부 탐색 X
# 이분 탐색을 통해 시간복잡도를 N*logN 으로 줄여야 한다.

from sys import stdin
read = stdin.readline

# 문제의 최소 범위보다도 더 작은 수
INF = -1000000001

# 수열의 크기
N = int(read())
nums = list(map(int,read().split()))
LIS = [INF]
LIS_total = [[INF,0]]

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    # 같은 숫자가 들어올 수도 있기에 
    while start < end:
        mid = (start + end) // 2

        if target > arr[mid]:
            start = mid + 1
        else:
            end = mid

    return end

for num in nums:
    # 수열을 순회하며 나오는 숫자가 LIS의 마지막 원소 보다 크다면
    if num > LIS[-1]:
        LIS_total.append([num, len(LIS)])
        LIS.append(num)

    else:
        idx = binary_search(LIS, num)
        LIS[idx] = num
        LIS_total.append([num, idx])

# LIS 완성 -> 역추적 시작
result = []
LIS_length = len(LIS) - 1

while LIS_total and LIS_length:
    num, idx = LIS_total.pop()

    if idx == LIS_length:
        result.append(num)
        LIS_length -= 1

print(len(result))
print(*result[::-1])