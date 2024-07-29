a = input()

b = int(input())

c = []

for i in range(b):
    d = input().split()
    c.append(d)

f = 0
g = 0
for e in c:
    f += 1
    if a in e:
        g = f
        break
if g == 0:
    g = -1
print(g)