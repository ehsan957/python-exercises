# def factorial(num):
#     factorial = 1
#     while num > 1:
#         factorial = factorial * num
#         num = num - 1
#     return factorial

def factorial(num):
    if num==0:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(5))
print(factorial(2))
print(factorial(3))
print(factorial(20))