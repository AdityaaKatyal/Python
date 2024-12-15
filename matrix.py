mat  = []
n = int(input("Enter no. of rows:"))
m = int(input("Enter no. of columns:"))
for i in range (n):
    a = []
    for j in range (m):
        a.append(int(input("Enter elements:")))
    mat.append(a)

for k in mat:
    print(*k)