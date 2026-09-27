while True:
    n = int(input())
    if n in (0, 3):
        print("Exit" if n == 0 else "Correct")
        break
    print("High" if n > 3 else "Low")