lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	lst.append(ele) 

s = set(lst)

print(s)