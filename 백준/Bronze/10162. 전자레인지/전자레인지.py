# 백준 10162 전자레인지
import sys
read= sys.stdin.readline

n = int(input())

if (n % 10) != 0:
	print(-1)
	
else:
	for i in [300, 60, 10]:
		print(n//i, end=' ')
		n = n%i