A = list(map(int, input().split()))
a = str(A[0])
b = str(A[1])
j = len(a)
k = len(b)
l = min(a, b)
g = 0

for i in range(1, len(l)+1):
    c = -(i)
    d = a[c]
    e = b[c]
    f = int(d) + int(e)
    if len(str(f)) > 1:
        g += 1
        break
    else:
        pass

if g > 0:
    print("Hard")
else:
    print("Easy")
