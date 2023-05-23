# 백준 3649 로봇 프로젝트
import sys
read = sys.stdin.readline

while True:
    try:
        # 구멍의 너비 (1 <= x <= 20), 나노미터로 계산할거니까 천만 곱하기.
        x = int(read()) * 10000000

        # 레고 조각의 수 (0 <= n <= 1,000,000), 레고 조각의 길이를 담은 배열 (단위는 나노미터)
        n = int(read())
        lego = list()

        # 레고 조각이 하나거나 0개이면 문제를 해결 할 수 없음.
        if n == 0:
            print('danger')
            continue

        elif n == 1:
            lego.append(int(read()))
            print('danger')
            continue

        for _ in range(n):
            # 레고 조각의 길이는 항상 나노미터로 주어짐 (1cm = 10,000,000 nm), 10cm는 넘지 않음
            lego.append(int(read()))

        # 투 포인터 알고리즘을 사용하기 위해 정렬
        lego.sort()
        idx = 0
        iidx = n-1

        # 투 포인터 시작
        while True:
            # 정답이 여러개 일수 있지만, 처음 나온 두 조각이 abs(a-b) 값이 가장 크다. (정렬된 값이니까?)
            if lego[idx] + lego[iidx] == x:
                print('yes %d %d' %(lego[idx], lego[iidx]))
                break

            elif lego[idx] + lego[iidx] > x:
                iidx -= 1

            elif lego[idx] + lego[iidx] < x:
                idx += 1

            if idx == iidx:
                print('danger')
                break

    except:
        break