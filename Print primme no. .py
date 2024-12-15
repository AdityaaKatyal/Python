n = int(input("Enter the lower limit:"))
m = int(input("Enter the upper limit:"))

for p in range (n, m+1):
    if p > 1:
        for i in range (2, p):
            if (p%i) == 0:
                break
        else:
            print(p)