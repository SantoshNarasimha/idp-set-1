a = list(map(int, input().split()))
f = 0

for num in a:
    if int(num) < 10:
        pass
    else:
        b = len(str(num))
        d = str(num)
        c = d[b - 1]
        c = int(c)
        e = d[:b - 1]
        e = int(e)
        z = e ** c
        f += z
print(f)