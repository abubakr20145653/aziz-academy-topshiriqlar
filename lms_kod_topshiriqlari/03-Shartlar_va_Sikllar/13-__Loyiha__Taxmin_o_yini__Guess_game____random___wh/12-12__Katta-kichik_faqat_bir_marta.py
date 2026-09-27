while True:
    n = int(input())
    print("Correct" if n == 8 else ("Low" if n < 8 else "High"))
    if n == 8:
        break