n = int(input())
for _ in range(n):
    if (x := int(input())) % 7 == 0:
        print(x)
        break
else:
    print("yo'q")