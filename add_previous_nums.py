s = int(input("Enter the range: "))

v = [1, 1]

for i in range(1, s-1):
    z = v[i-1] + v[i]
    v.append(z)
print(v)



