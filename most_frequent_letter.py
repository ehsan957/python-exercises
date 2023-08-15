text = "islamic republic of iran yazd bafgh"
letter_list = []
for letter in text:
    counter = 0
    for l in text:
        if l==letter:
            counter += 1
    letter_list.append([counter, letter])



letter_list.sort(reverse=True)

seq = []
for i in letter_list:
    seq.append(i[1])

seq_length = len(seq)
i = 0
uniqe_list = []
check = seq[0]
while i<seq_length:
    if i==0 or seq[i] != check:
        uniqe_list.append(seq[i])
        check = seq[i]
    i += 1

print(uniqe_list)
