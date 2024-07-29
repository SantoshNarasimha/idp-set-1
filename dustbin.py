a = [3, 1, 6, 7]


for j in range(len(a)-1):
    for i in range(len(a) - 1):
        if a[j] < a[i]:
            a[j], a[i] = a[i], a[j]

print(a)