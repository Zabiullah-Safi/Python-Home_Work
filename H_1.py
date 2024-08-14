# factorial

def factorial(n):
    count = 1
    if n < 0:
        return "factorial not defined for negative numbers"
    elif n == 1 or n == 0:
    else:
        for i in range(2, n+1):
            count *= i
        return count

n = int(input("Enter a number:"))
print(factorial(n))
        
