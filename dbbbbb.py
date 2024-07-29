"""a = list(input().split())

h = a.copy()

for i in range(len(a)):

    b = a[i]
    d = ""
    for c in a[i+1: ]:
        e = b + c
        if len(b) == 1:
            if e == e[::-1]:
                u = a.index(c)
                #print(u)
                print(a.index(b), a.index(c, u+1))
        else:
            if e == e[::-1]:
                print(a.index(b), a.index(c))

h.reverse()
j = []
k = []

for i in range(len(h)):

    b = h[i]
    d = ""
    for c in h[i+1: ]:
        e = b + c
        if e == e[::-1]:
            l = a.index(b)
            m = a.index(c)
            j.append(l)
            k.append(m)

p = len(j) - 1

for o in range(len(j)):
     print(j[p], k[p])
     p = p -1

"""

v = []

n = int(input())

for i in range(n):
    w = input()
    v.append(w)

y = []
m = ""
z = 0
max_length = max(len(x.split()) for x in v)
for i in range(max_length):
    for x in v:
        k = x
        k = k.split()
        l = len(k)
        x = x.split()
        if z < l:  # Change the condition to 'if z < l:'
           a = x[z]
           if a is not None:
               m = m + a
           z = z + 1

    y.append(m)
    m = ""
    l = 0
    a = ""
    z = 0


for u in y:
    print(u)









