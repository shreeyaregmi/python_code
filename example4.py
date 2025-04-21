example = list(range(1,11))
print("list", example)

for i in range(len(example)):
    if example[i]%2 ==0:
        example [i] = 0
    else:
     example [i] = -1
print ("changed", example)