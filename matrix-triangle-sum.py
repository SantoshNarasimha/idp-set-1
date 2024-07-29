n = int(input())

k = []

for i in range(n):
    v = list(map(int, input().split()))
    k.append(v)

count = []
j = -1
for num in k:
    j +=1
    n = len(num)
    for i in range(1):
        count.append(num[:n-j])


p = 0
for o in count:
    p += sum(o)
print(p)



m = 0
hm = []
for num in k:
    m +=-1
    for i in range(1):
        hm.append(num[m:])
p = 0
for o in hm:
    p += sum(o)
print(p)