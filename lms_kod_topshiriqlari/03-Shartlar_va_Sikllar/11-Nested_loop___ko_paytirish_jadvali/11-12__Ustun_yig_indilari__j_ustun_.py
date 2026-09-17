n, m = map(int, input().split())
for j in range(1, m + 1):
    ustun_yigindisi = sum(i * j for i in range(1, n + 1))
    print(ustun_yigindisi)