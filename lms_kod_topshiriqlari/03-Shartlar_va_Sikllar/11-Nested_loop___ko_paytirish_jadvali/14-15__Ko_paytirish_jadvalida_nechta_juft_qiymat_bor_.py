import sys 
n, m = map(int, sys.stdin.read().split())
top = ((n + 1) // 2) * ((m + 1) // 2)
print(n * m - top)