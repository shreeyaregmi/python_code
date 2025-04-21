def findMax(mylist):
    min = mylist[0]
    for i in mylist:
        if i < min:
            min = i
    max = mylist[0]
    for i in mylist:
        if i > max:
            max = i
    return min, max 
print(findMax ([3,6,9,11,5]))