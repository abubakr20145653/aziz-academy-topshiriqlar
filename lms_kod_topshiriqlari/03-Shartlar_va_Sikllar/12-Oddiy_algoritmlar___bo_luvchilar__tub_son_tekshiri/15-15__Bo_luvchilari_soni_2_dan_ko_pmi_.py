n = int(input())

has_more_than_2 = False
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        has_more_than_2 = True
        break
        
print("Yes" if has_more_than_2 else "No")