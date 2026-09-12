s = input()
k = 0
for ch in s:
    if ch in "aeiou":
        k += 1
print(k)