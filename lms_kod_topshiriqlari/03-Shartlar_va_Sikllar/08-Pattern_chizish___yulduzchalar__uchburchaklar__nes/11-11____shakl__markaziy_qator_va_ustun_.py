n = int(input())
m = n // 2
for i in range(n):
    print("".join("*" if i == m or j == m else "." for j in range(n)))