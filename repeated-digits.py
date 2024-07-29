gundey = input()

gundey = list(gundey)

naya = set(gundey)

naya = list(naya)

count = 0

for i in range(len(naya)):
    kaya = naya[i]
    if gundey.count(kaya) > 1:
        count += 1
print(count)

"""
input : 212311
output: 2
"""