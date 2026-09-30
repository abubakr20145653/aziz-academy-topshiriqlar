# To‘liq menyu tuzing: 1..6 amallar, 0 chiqish.
# while + if/elif/else ishlating.
a, b = map(int, input().split())
while (n := int(input())) != 0:    
    if n == 1: print(a + b)
    elif n == 2: print(a - b)
    elif n == 3: print(a * b)
    elif n == 4: print(a / b)
    elif n == 5: print(a // b)
    elif n == 6: print(a % b)
print("Exit")