a = input().split()

b = ""
c = []
w = []
f = -1

for u in a:
    v = len(u)
    w.append(v)
    
for d in range(max(w)):
    f +=1
    for e in a:
        if len(e) > f:
            b += e[f]
        else:
            b += " "
    c.append(b)
    b = ""

for t in c:
    print(t)