for i in range(1,51):
    e=i
    c = 0
    while e:
        c += 1
        e &= e - 1
    if (c%2)== 1:
        print(i)


