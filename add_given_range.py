two = list(map(int, input("enter the size and nth smallest value\n").split()))

san = int(input("Enter how many range of numbers you want to take: "))

for i in range(san):
    tej = list(map(int, input("enter the range\n").split()))
    v = 0
    for j in range(tej[0], tej[1]+1):
        v += two[j]
    print(v)
"""
if input is 0 2
it will add numbers which are in position[index] of 0 1 & 2
"""