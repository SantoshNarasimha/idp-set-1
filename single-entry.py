shiva = list(map(int, input().split()))

v = len(shiva)

for i in range(v):
    mm = shiva[i]
    ssss = shiva.count(mm)
    if ssss == 1:
        print(shiva[i])