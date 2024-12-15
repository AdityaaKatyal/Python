def unique(list): 
    uni = [] 
    for i in list:
        if i not in uni:
            uni.append(i)
    return uni

list = [1,1,2,2,3,4,5,6,10,1,5,9]

s = unique(list)
s.sort()
print(s)



