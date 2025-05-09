from math import sqrt

def isPrime(n):
    if n < 2: 
        return False  
    
    for i in range(2, int(sqrt(n)) + 1):  
        if n % i == 0:
            return False
    
    return True

n = int(input("Enter a number: "))
if isPrime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")