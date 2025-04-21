#calculate the power 
def powof(x, y):
    if y == 0:
        return 1
    else:
        return x * powof (x, y-1)
    
print("the power : ", powof(2,3))
