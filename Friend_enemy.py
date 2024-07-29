s = list(map(int, input().split()))
a_min = min(s)
b_max = len(s)

new_list = [number for number in range(a_min, b_max + 1)]


def difference_keywords(s, new_list):
    difference = [keyword for keyword in new_list if keyword not in s]
    return difference


e = difference_keywords(s, new_list)

for i in range(a_min, b_max):
    counts = s.count(s[i])
    if counts > 1:
        f = s[i]
        break

print(str(f) +  " " + str(e[0]))
