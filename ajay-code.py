a = 12345654321
a = str(a)
b = list(a)


c = b[0]
n = len(b)
d = b[n-1]

b = [int(x) for x in b]
e = sum(b[1:n-1])
e = str(e)


g = c + d + e
print(g)