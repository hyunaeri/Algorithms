# 백준 2805 나무 자르기
import sys
read = sys.stdin.readline

# 나무의 수, 집으로 가져가려고 하는 나무의 길이
N,M = map(int,read().split())
trees = sorted(list(map(int,read().split())))
max_cut = trees[-1]

# 잘리는 나무의 인덱스를 리턴
def binary_search(start, end):
    while start <= end:
        mid = (start+end) // 2
        cutting_length = 0

        # mid 보다 더 큰 나무들은 다 잘린다
        for tree in trees:
            if tree > mid:
                cutting_length += (tree-mid)

        # 원하는 양보다 더 많이 잘렸으면
        if cutting_length > M:
            start = mid + 1

        # 원하는 양만큼 잘렸으면
        elif cutting_length == M:
            return mid

        # 원하는 양보다 덜 잘렸으면
        else:
            end = mid - 1

    return end

print(binary_search(0, max_cut))
