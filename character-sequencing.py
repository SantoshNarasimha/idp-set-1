s = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

p = list(map(int, input().split()))

z = ""

for i in range(len(p)):
    v = p[i]
    k = s[v]
    z += k
print(z)