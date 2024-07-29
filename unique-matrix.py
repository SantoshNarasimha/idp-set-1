n = int(input())

k = []

for i in range(n):
    v = list(map(int, input().split()))
    k.append(v)

hm = 0
for num in k:
    g = sorted(num)
    a = 1
    b = n
    j = 0
    for i in range(a, b+1):
        if g[j] != i:
            hm +=1
            break
        else:
            j +=1

if hm >=1:
    print("False")
else:
    print("True")