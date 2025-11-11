# 백준 14891
# 골드 5
# https://www.acmicpc.net/problem/14891

import sys
read = sys.stdin.readline

def rotate(gear, dir):
    if dir == 1: return gear[-1] + gear[:-1]
    else: return gear[1:] + gear[0]

def calc_score(gear_info):
    weights = [1, 2, 4, 8]
    answer = 0
    for idx, gear in enumerate(gear_info):
        if gear[0] == '1':   # 입력은 '0'/'1' 이므로 '1'이 S극
            answer += weights[idx]
    return answer

def debug(info):
    for gear in info:
        print(f"original gear : {gear}")
        print(f"clockwise rotate gear : {rotate(gear, 1)}")
        print(f"counterclockwise rotate gear : {rotate(gear, -1)}")
        print("======================")

if __name__ == "__main__":
    # 4개의 톱니바퀴 상태 ('0' : N, '1' : S)
    gear_info = [ read().rstrip() for _ in range(4) ]

    K = int(read())
    rotate_info = [ list(map(int, read().split())) for _ in range(K) ]

    # 디버깅
    # debug(gear_info)

    for info in rotate_info:
        gear_num = info[0] - 1 
        rotate_dir = info[1]

        # 현재 상태 스냅샷 (전파 판단은 스냅샷 기준)
        snapshot = gear_info[:]

        # 각 기어의 회전 방향 미리 결정 (0은 회전 불가능)
        dirs = [0, 0, 0, 0]
        dirs[gear_num] = rotate_dir

        # 왼쪽 전파
        for i in range(gear_num, 0, -1):
            if snapshot[i][-2] != snapshot[i - 1][2]:
                dirs[i-1] = dirs[i] * -1
            else:
                break

        # 오른쪽 전파
        for i in range(gear_num, 3):
            if snapshot[i][2] != snapshot[i + 1][-2]:
                dirs[i + 1] = dirs[i] * -1
            else:
                break

        # 결정된 방향대로 동시에 회전 적용
        for i in range(4):
            if dirs[i] != 0:
                gear_info[i] = rotate(gear_info[i], dirs[i])

    print(calc_score(gear_info))