T = int(input("Enter how many times you want to run the code= "))

for i in range(T):
    kam = ""
    k = int(input("Enter how many names you want to insert= "))
    for j in range(k):
        f = input("Enter the name= ")
        kam += f + ","
    kam = kam.split(',')
    naam = 0
    for o in range(len(kam)):
        for l in range(o + 1, len(kam)):
            if kam[l] == kam[o]:
                naam +=1
    if naam >=1:
        print("Yes")
    else:
        print("No")