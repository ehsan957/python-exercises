max = int(input("Enter a first number: "))
min = int(input("Enter a second number: "))
#I should find maximum number
if min > max:
    #we swap the munbers
    min,max = max, min

multiply = 1

while True:
    if (max * multiply)%min == 0:
        print(max*multiply)
        break
    multiply += 1
