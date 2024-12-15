mat1  = []
n = int(input("Enter no. of rows:"))
m = int(input("Enter no. of columns:"))
for i in range (n):
    a = []
    for j in range (m):
        a.append(int(input("Enter elements:")))
    mat1.append(a)

mat2  = []
n1 = int(input("Enter no. of rows:"))
m1 = int(input("Enter no. of columns:"))
for i in range (n1):
    b = []
    for j in range (m1):
        b.append(int(input("Enter elements:")))
    mat2.append(b)

if n == n1 and m == m1:
    print("Result of addition is:")
    output = []

    for i in range (n1):
        result = []
        for j in range (m1):
            result.append(mat1[i][j] + mat2[i][j])
        output.append(result)
    for a in output:
        print(*a)
else:
    print("Rows and columns must be same for addition")