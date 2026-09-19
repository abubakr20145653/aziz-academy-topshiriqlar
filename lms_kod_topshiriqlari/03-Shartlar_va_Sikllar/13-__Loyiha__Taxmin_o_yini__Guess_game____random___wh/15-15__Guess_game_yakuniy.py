target = 20
count = 0
while True:
    num = int(input())
    count += 1
    if num < 1 or num > 20:
        print("Invalid")
    elif num < target:
        print("Low")
    elif num > target:
        print("High")
    else:
        print("Correct")
        break
print(count)