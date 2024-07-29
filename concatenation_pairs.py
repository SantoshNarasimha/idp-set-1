v = []
n = int(input())

for i in range(n):
    w = input()
    v.append(w)

y = []
m = ""
z = 0

# Find the maximum length among all the strings
max_length = max(len(x.split()) for x in v)

for i in range(max_length):
    for x in v:
        k = x.split()
        if z < len(k):
            a = k[z]
            m = m + a
    y.append(m)
    m = ""
    z += 1

for u in y:
    print(u)