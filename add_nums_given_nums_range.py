def main():
    shiva = list(map(int, input("Enter the numbers: ").split()))
    beauty = int(input("Enter how many times you want to insert the range: "))
    pandaa(shiva, beauty)


def pandaa(shiva, beauty):
    for i in range(beauty):
        ranges = list(map(int, input("Enter").split()))
        vm = ranges[0]
        vk = ranges[1]
        v = 0
        for j in range(vm, vk + 1):
            if j in shiva:
                counts = shiva.count(j)
                v += (j * counts)
        print(v)


if __name__ == '__main__':
    main()


"""
Enter the numbers: 2 1 2 2 3 3 4 5 5 6 7 
Enter how many times you want to insert the range: 2
Enter0 2
7         #number of 2's are 3 = 6, number of 1's are = 1
Enter1 7
40

"""