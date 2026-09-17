n, m = map(int, input().split())
for i in range(1, n + 1):
    qator_yigindisi = sum(i * j for j in range(1, m + 1))
    print(qator_yigindisi)