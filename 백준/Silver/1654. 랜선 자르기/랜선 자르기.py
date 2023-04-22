# 백준 1654 나무자르기
import sys
read = sys.stdin.readline

# 이미 가지고 있는 랜선의 개수, 필요한 랜선의 개수
M,N = map(int,read().split())
lans = sorted([int(read()) for _ in range(M)])
max_lan = lans[-1]

def binary_search(target, start, end):
    while start <= end:
        mid = (start+end) // 2
        answer = 0

        for lan in lans:
            answer += (lan // mid)

        # 필요한 개수보다 더 많이 만든 경우
        if answer >= target:
            start = mid + 1

        # # 필요한 만큼만 만든 경우
        # elif answer == target:
        #     return mid
        
        # 필요한 개수보다 덜 만든 경우
        else:
            end = mid - 1

    # 딱 필요한 만큼은 못만듬,
    # 그래서 필요한 개수에 가장 가까운 값
    return end

print(binary_search(N, 1, max_lan))