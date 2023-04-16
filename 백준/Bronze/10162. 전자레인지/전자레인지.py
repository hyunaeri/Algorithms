# 백준 10162 전자레인지
import sys
read= sys.stdin.readline

T = int(read())
button = dict()
button[300], button[60], button[10] = 0, 0, 0
cnt = 0

while True:
    if T >= 300:
        button[300] += 1
        T -= 300
    elif 60 <= T < 300:
        button[60] += 1
        T -= 60
    elif 10 <= T < 60:
        button[10] += 1
        T -= 10
    else:
        break

if T ==0:
    for value in button.values():
        print(value, end=' ')
else:
    print(-1)
