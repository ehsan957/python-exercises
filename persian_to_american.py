score = int(input("Please enter your score: "))

if score>=17:
    print("A",end="",)
    if score>19:
        print("+")
elif score>=14:
    print("B")
elif score>=12:
    print("C")
elif score>=10:
    print("D")
else:
    print("F")