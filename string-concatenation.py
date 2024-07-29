A = input().split()
B = input().split()
C = input().split()
D = []
E = A + B + C

F = list(input())


n = ""
for i in range(0, len(F)):
  K = int(F[i])
  m = E[K-1]
  n +=m
print(n)