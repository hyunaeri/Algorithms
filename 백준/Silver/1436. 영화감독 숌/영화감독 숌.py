import sys

input = sys.stdin.readline

n = int(input())
count = 0
end_number = 666

while True:
    if '666' in str(end_number):
        count += 1
    
    if count == n:
        print(end_number)
        break

    end_number += 1