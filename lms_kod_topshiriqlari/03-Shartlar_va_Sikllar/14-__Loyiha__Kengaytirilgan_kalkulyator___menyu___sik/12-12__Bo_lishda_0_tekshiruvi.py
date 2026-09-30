# Agar bo‘lishda b=0 bo‘lsa "Error" chiqaring.
a, b = map(int, input().split())
if b == 0:
    print("Error")
else:
    print(a / b)