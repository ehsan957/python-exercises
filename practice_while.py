sum = 0
count = 0
while True:
    score = int(input("Enter score: "))
    if score == -1:
        break
    sum = sum+score
    count = count + 1
print("The average is: ", sum/count)