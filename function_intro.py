def divisors(x):
    div = []
    for i in range(1, x+1):
        if x%i == 0:
            div.append(i)
    return div

def isPrime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def primDivisors(y):
    primDiv = []
    for x in divisors(y):
        if isPrime(x):
            primDiv.append(x)
    return primDiv



num1 = int(input("Enter a number: "))
print(primDivisors(num1))






