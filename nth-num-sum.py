ncdex = list(map(int, input().split())) # range

ncdexx = list(map(int, input().split()))# values

ok = ncdex[0]
hm = ncdex[1]

v = len(ncdexx)

k = 0

for i in range(1,v+1):
  okk = i % ok
  if okk == 0:
    k += ncdexx[i-1] # the index will be staring from 0 and we have taken range from 0 in for loop
      # so we have taken i-1
print(k)