
def fact_recr(n):
    if n == 1:
        return 1
    else:
        return n * fact_recr(n-1)
    
try:
    num = int(input("enter a number:"))
    print("Factorial from top down function:", fact_recr(num))
except ValueError as e:
    print("OOPS!", e)
print("Factorial from the recursive function:", fact_recr(num))
