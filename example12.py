def findList(list):
    max_number = list[0]
    for num in list:
        if num > max_number:
            max_number = num 
    return max_number
the_list = [3,6,2,7,1,9,4]
print(findList(the_list))
    
    