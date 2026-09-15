n = int(input())
count = 0
for _ in range(n):
    son = int(input())
    if son % 3 == 0:
        count += 1
print(count)