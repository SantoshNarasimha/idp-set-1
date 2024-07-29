n = int(input())

count = []
for i in range(n):
    k = list(map(int, input().split(',')))
    count.append(k)
ok = []

for j in range(n):
    y = sum(count[j])
    ok.append(y)
print(type(ok))
ok = [int(x) for x in ok]
print(type(ok))
k = ok.index(max(ok))
hm = count[k]
ko = " ".join([str(integer) for integer in hm])
print(hm)