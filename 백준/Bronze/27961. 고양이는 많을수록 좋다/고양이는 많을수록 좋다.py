# 백준 27961 고양이는 많으면 많을수록 좋다
import sys
read = sys.stdin.readline

n = int(read())
cnt = 2
x, y = 1, 2

while True:
    if n == 0:
        print('0')
        break
    elif n == 1:
        print('1')
        break
    else:
        if x < n <= y:
            print(cnt)
            break
        else:
            cnt += 1
            x *= 2
            y *= 2
    