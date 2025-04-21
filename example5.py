numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
print("Numbers:", numbers)

evenSum = 0
oddSum = 0

for i in numbers: 
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i

# Print sums after the loop
print("Sum of even numbers:", evenSum)
print("Sum of odd numbers:", oddSum)

# Compare sums
if evenSum > oddSum:
    print("Even sum is greater.")
else:
    print("Odd sum is greater.")

            
            