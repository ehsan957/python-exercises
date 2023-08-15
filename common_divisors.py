num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
min = num1
if num2<min:
    min = num2
c = 2
divisors = []
while c<=min:
    if num1%c == 0 and num2%c == 0:
        divisors.append(c)
    c += 1
print("Comon divisors of ", num1, num2, " are: ", divisors)