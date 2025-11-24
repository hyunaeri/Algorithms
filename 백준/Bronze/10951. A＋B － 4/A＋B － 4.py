import sys
read = sys.stdin.readline

while True:
    buf = read()
    
    if buf == '':
        exit(0)
        
    A, B = buf.split()
    
    print(int(A) + int(B))

