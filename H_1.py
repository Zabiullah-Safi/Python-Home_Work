
# 11: Create a class Account with private attributes balance. Provide public methods to deposit
# and withdraw money.

class Account:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(sefl, deposit):
        self.__balance += deposit

    def withdraw(self, withdraw):
        sefl.__balance -= withdraw
    
    def get(self):
        return self.__balance

account = Account(50000)
account.deposit(4000)
account.withdraw(10000)
print(account.get())




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
        
