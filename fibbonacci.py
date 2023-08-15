# num1 = 0
# num2 = 1

# count = 1

# while True:
#     print(num1)
#     c = num1+num2
#     num1 = num2
#     num2 = c
#     print(count)
#     count += 1
import time
def fibbonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)


counter = 1
while True:
    fi = fibbonacci(counter)
    print(fi)
    counter += 1
    time.sleep(.1)