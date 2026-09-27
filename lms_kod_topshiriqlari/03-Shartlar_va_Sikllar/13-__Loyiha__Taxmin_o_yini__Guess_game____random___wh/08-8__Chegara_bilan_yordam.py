while True:
    n = int(input())
    if n == 15:
        print("Correct")
        break
    print("Far" if abs(15 - n) >= 5 else "Close")