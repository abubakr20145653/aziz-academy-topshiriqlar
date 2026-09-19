n = int(input())
print("MUKAMMAL" if n > 1 and sum(i for i in range(1,n) if n % i == 0) == n else "MUKAMMAL EMAS")