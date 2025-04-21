def is_palindrome(s):
    
    if len(s) <= 1:
        return True
    
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


text = input("Enter a string: ").lower().replace(" ", "")   


if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


def fib(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return fib(n - 1) + fib(n - 2)

# Taking input from the user
num = int(input("Enter the position (n) in the Fibonacci sequence: "))

# Getting the nth Fibonacci number
result = fib(num)

# Printing the result
print(f"fib({num}) = {result}")
