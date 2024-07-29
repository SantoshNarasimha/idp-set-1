san = input()

sab = list(map(int, input().split()))

new_count = ""

for i in range(len(sab)):
    count = 0
    for j in range(i+1, len(sab)):
        if sab[i] > sab[j]:
            count += 1
    new_count += str(count) + " "
print(new_count)

"""
//
3
1 2 3 4
0 0 0 0 

//
3
13 12 11
2 1 0 

//
4
4 3 5 2
2 1 1 0 

4 got highest marks more than 3 and 2
3 got highest marks more than 2
5 got highest marks more than 2

"""