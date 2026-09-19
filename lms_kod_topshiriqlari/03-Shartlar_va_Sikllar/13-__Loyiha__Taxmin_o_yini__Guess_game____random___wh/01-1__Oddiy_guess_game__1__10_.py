while True:
    n = int(input())
    if n == 7:
        print("Correct")
        break
    print("Low" if n < 7 else "High")