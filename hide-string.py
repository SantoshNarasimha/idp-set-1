n = input().split()

small = ['a', 'b','c','d', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
large = []
for i in small:
    b = i.upper()
    large.append(b)

v = ""
for nan in n:
    j = ""
    for i in range(len(nan)):
        s = nan[i]
        if s in small:
            g = small.index(s)
            h = small[g - 1]
            j += h
        else:
            x = large.index(s)
            y = large[x - 1]
            j += y
    v += j + " "
print(v)
