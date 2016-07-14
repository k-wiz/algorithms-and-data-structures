def first_factorial(num): 
    """Takes a num and returns the factorial of that num."""
    
    result = 1
    
    for i in range(1, num+1):
        result = result * i
        print num, result
    
    return result


print first_factorial(8)
print first_factorial(1)
print first_factorial(4)