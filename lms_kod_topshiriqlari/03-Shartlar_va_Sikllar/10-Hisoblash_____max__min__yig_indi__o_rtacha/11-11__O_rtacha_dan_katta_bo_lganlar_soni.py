n = int(input())
sonlar = list(map(int, input().split()))
orta = sum(sonlar) / n
print(sum(1 for x in sonlar if x > orta))