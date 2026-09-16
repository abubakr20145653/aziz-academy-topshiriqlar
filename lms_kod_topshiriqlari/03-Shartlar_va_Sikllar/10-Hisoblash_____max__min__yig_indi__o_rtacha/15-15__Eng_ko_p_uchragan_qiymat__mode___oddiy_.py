from collections import Counter
input()
c = Counter(map(int, input().split()))
print(min(c, key=lambda x: (-c[x], x)))