n = int(input())
t = int(input())
hisob = 0
for  i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i * j) % t == 0:
            hisob += 1
print(hisob)