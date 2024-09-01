def calculate_factorial(n):
    
    if isinstance(n, int):
    
        if n < 0:
            return "Factorial is not defined for negative numbers."
        
        elif n == 0 or n == 1:
            return 1
        else:
        
            factorial = 1
            for i in range(2, n + 1):
                factorial *= i
            return factorial
    else:
        return "Input is not an integer."


print(calculate_factorial(7)) 
