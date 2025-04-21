import time
def factorial_recursive(n):
    if n == 0:
        return 1
    else: 
        return n * factorial_recursive(n-1)
    
def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result 

n = 100

start_time = time.time()
factorial_recursive(n)
end_time = time.time()
recursive_time = end_time - start_time

start_time = time.time()
factorial_iterative(n)
end_time = time.time()
iterative_time = end_time - start_time

print(f"Recurisve approach took {recursive_time:.10f} sceonds")
print(f"Iterative approach took {iterative_time:.10f} sceonds")
