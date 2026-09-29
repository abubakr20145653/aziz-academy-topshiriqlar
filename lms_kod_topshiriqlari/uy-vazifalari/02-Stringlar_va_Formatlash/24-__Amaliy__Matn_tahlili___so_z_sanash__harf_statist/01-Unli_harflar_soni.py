matn = input().lower()
print(sum(matn.count(u) for u in "aeiou"))