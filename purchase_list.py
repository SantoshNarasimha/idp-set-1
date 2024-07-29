a = list(map(int, input().split()))

for i in range(len(a)):
    c = a[i]
    b = a.count(c)
    g = ""
    if b == 1:
        g = c
        break
    else:
        pass

if g == "":
    print("None")
else:
    print(g)

for i in range(len(a)):
    c = a[i]
    b = a.count(c)
    g = ""
    if b > 1:
        g = c
        break
    else:
        pass

if g == "":
    print("None")
else:
    print(g)