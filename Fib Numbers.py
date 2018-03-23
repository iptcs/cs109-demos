n = 100
fibnums = []

i = 0
while i < n:
    if len(fibnums) < 2:
        fibnums.append(1)
    else:
        next_fibnum = fibnums[-1] + fibnums[-2]
        fibnums.append(next_fibnum)
    i = i + 1


print(fibnums)
