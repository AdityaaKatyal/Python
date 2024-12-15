n = int(input("Enter a value:"))
flag = False
if n ==1 or n == 0:
    print(n, "is not prime")
elif n>1:
    for i in range (2, n):
        if (n%i) == 0:
            flag = True
            break
    if flag:
        print(n,"is not prime")
    else:
        print(n, "is prime") 
        


    