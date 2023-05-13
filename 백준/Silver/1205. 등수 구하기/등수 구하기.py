# 백준 1205 등수 구하기
import sys
read = sys.stdin.readline

# N개의 점수, 새로운 점수, 랭킹 리스트에 올라가는 최대 갯수
N, new_score, P = map(int,read().split())

if N != 0:
    ranking = [0] + list(map(int,read().split()))

    # 이미 랭킹 리스트가 꽉참. 랭킹 리스트의 마지막 순위 값과 비교해 새로운 점수가 작거나 같으면 랭킹 갱신 불가
    if N == P and ranking[-1] >= new_score:
        print(-1)

    else:
        for i in range(1, N+1):
            if new_score >= ranking[i]:
                print(i)
                exit()
                
        print(N+1)

else:
    print(1)