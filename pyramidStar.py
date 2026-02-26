for i in range(5):
    for j in range(9):
        end = i+4
        start = 4-i
        # print(f'start {start}, end: {end}, j: {j}')
        if j >= start and j <= end:
            print("*",end="")
        else:
            print(" ",end="")
    print("")