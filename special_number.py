s = input()
k = s.split(" ")

result = [[int(digit) for digit in str(number)] for number in k]

v = []

for p in result:
    for i in range(1):
        c = p[0] % 2
        if c == 0:
            for j in range(1, len(p)):
                c = p[j] % 2
                if c == 0:
                    pass
                else:
                    p = p[j: ] + p[0: j]
                    v.append(p)
                    break
            else:
                if all(num%2 == 0 for num in p):
                    v.append(p)
        else:
            v.append(p)
result = ' '.join([''.join(map(str, sublist)) for sublist in v])
print(result)
