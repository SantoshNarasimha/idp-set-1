sann = input()

san = sann.split(",")

k = '00'

for i in range(len(san)):
  if san[i] == k:
    san[i] = '0'
print(san)
van = int(input())

mar = san[van:]

aar = san[:-van]


"""
printing last n numbers and first n numbers
"""


print(" ".join(map(str, mar)))
print(" ".join(map(str, aar)))