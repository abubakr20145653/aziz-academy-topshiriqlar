n = int(input())
products = []
for _ in range(n):
    name, count = input().split()
    products.append({'name': name, 'count': int(count)})
x, k = input().split()
k = int(k)
for p in products:
    if p['name'] == x:
        p['count'] = p['count'] - k
for p in products:
    print(p['name'], p['count'])