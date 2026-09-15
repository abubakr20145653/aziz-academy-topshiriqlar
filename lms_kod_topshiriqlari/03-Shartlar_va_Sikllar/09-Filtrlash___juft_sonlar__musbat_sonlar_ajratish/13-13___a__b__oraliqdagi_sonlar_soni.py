n = int(input())
a = list(map(int, input().split()))
l, r = map(int, input().split())
print(sum(l <= x <= r for x in a))