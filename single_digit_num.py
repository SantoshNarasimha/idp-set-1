"""
a = ['was', 'it', 'a', 'car', 'or', 'a', 'cat', 'I', 'saw']

count = 0
for i in range(len(a)):
    b = a[i]
    for k in a[i+1:]:
        j = k[::-1]
        if b == j:
            if len(b) == 1:
                z = a.index(k)
                v = a.index(k, z+1)
                print(z, v)
            else:
                print(a.index(b), a.index(k))
"""


n = int(input())

p = []
for i in range(n):
    v = list(map(int, input().split()))
    p.append(v)

l = []
a = p
o = 0
for k in p:
    k_copy = k[:]  # Make a copy of the current element
    del k_copy[o]
    o += 1
    l.append(k_copy)

r = -1
for q in a:
    print(q)
    r = r - 1
























