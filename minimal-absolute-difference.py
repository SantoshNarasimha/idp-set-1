n = list(map(int, input().split()))

v = []

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        x = abs(n[i])
        y = abs(n[j])
        k = y - x
        p = abs(k)
        j = str(p)
        v.append(j)
min_value = min([int(element) for element in v])
print(min_value)


