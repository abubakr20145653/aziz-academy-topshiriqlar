while True:
    n = int(input())
    if n == -4:
        print("Correct")
        break
    print("High" if n > -4 else "Low")