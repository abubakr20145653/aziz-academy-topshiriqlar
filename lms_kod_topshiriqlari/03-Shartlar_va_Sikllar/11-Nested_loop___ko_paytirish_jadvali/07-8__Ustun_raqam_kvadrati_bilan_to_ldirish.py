a, b = map(int, input().split())
qator = []
for i in range(a, b + 1):
    qator.append(str(i ** 2))
print(" ".join(qator))