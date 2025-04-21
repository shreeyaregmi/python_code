def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

num = int(input("Enter a number: "))


result = sum_of_digits(num)

print("Sum of the digits:", result)

#using base and recursive

def sum_of_digits(n):
    # Base case: when n is a single-digit number
    if n < 10:
        return n
    else:
        return (n % 10) + sum_of_digits(n // 10)

# Taking input from the user
num = int(input("Enter a number: "))

# Passing user input to the function
result = sum_of_digits(num)

# Printing the sum of digits
print("Sum of the digits:", result)


def digitsum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + digitsum(n // 10)
print ("Digitsum is :", digitsum(1234))