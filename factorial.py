# using if else 
def fact_norm(n):
    if n == 1:
        return 1
    else:
        return n * fact_norm(n - 1)
    
print("Factorial:", fact_norm(5))

# using for loop
def fact_norm(n):
    fact =1 
    for i in range(1,n+1):
        fact = fact * i
    return fact
print ("Factorial:", fact_norm(-2))

#using if else condition

#def fact_norm(n):
 #   if n < 0:
  #      raise ValueError("Factorial is not defined for negative values")
   # else:
    #    fact =1 
    #for i in range(1,n+1):
     #   fact = fact * i
    #return fact
#print ("Factorial:", fact_norm(-1)) 

#use the input from the user

def fact_norm(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Taking input from the user
num = int(input("Enter a number: "))

# Passing user input to the function
result = fact_norm(num)

# Printing the factorial
print("Factorial:", result)

def fact_norm(n):
    if n< 0:
        raise ValueError("Factorial is not defined for negative numbers")
    else:
        fact =1 
        for i in range (1, n+1):
            fact = fact * i 
        return fact 
try:
    num = int (input ("enter a number:"))
    print ("factorial :", fact_norm(num))
except ValueError as e:
    print ("oops!", e)
    
#multiply a number with the factorial.
def fact_recursive(n):
    if n==1:
        return 1 #base case
    else:
        return n*fact_recursive(n-1) #recurisve case