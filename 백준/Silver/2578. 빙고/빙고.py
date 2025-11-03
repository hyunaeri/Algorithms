# 백준 2578
# 실버 4
# https://www.acmicpc.net/problem/2578

import sys
read = sys.stdin.readline

# 5*5 빙고판 만들기
bingo = [ list(map(int, read().rstrip().split())) for _ in range(5) ]

def delete_num(target):
  for i in range(5):
    for j in range(5):
      if bingo[i][j] == target:
        bingo[i][j] = 0
        return i, j
      
def count_total_bingo(bingo):
    total = 0

    # 5개 행
    for i in range(5):
        ok = True
        for j in range(5):
            if bingo[i][j] != 0:
                ok = False
                break
        if ok: total += 1

    # 5개 열
    for j in range(5):
        ok = True
        for i in range(5):
            if bingo[i][j] != 0:
                ok = False
                break
        if ok: total += 1

    # 주대각
    ok = True
    for i in range(5):
        if bingo[i][i] != 0:
            ok = False
            break
    if ok: total += 1

    # 역대각
    ok = True
    for i in range(5):
        if bingo[i][4-i] != 0:
            ok = False
            break
    if ok: total += 1

    return total

answer = 0

while True:
  # 사회자가 부르는 수를 5개씩 저장
  num_list = list(map(int, read().rstrip().split()))

  for current_num in num_list:
    x, y = delete_num(current_num)
    answer += 1
    
    if count_total_bingo(bingo) >= 3:
      print(answer)
      exit(0)