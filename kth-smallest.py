def main(n, s, arr_1):
    arr_1.sort(reverse=False)  # small to big
    print(arr_1)
    print(arr_1[s - 1])


if __name__ == "__main__":
    n = list(map(int, input("enter the size and nth smallest value\n").split()))
    s = n[1]
    arr_1 = list(map(int, input("Enter elements of array\n").split()))
    main(n, s, arr_1)