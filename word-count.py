san = input("enter the string= ")
text = input("enter the repeating words: ")
k = san.split()
yarn = 0
for i in range(len(k)):
    if text == k[i]:
        yarn += 1
print(yarn)