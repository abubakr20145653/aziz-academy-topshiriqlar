n = int(input())
s = [x for x in map(int, input().split()) if x % 2 != 0]
print(max(s) if s else "No")