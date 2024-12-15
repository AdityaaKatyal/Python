f = {"Mango": 120,
     "Apple": 30,
     "Guava": 50
     }
for i in f:
    print(i, end=" ")
    print(f[i], sep=" ")

s = input()
freq = {}

for i in s:
    #print(i, end=" ")
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
print(freq)
