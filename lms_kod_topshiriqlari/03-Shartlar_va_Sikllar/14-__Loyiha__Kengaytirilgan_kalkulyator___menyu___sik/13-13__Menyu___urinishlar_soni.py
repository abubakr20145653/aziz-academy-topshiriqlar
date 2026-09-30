import sys
lines = sys.stdin.read().splitlines()
c = 0
for line in lines[1:]:
    parts = line.split()
    if len(parts) == 1:
        if parts[0] == '0':
            break
        c += 1
print(c)