num1 = int(input("Enter a number: "))
c = 2
divisors = []
while c<num1:
    if num1%c == 0:
        # print(c)
        divisors.append(c)
    c = c + 1

# print("The number of divisors of ", num1, "is ", divisors)
if len(divisors) == 0:
    print(num1," is a prime number")
else:
    print(num1," is NOT a prime number")