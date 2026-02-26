for i in range(5):
    for j in range(9):
        end = 8-i
        start = 8-end
        # print(f'start {start}, end: {end}, j: {j}')
        if j >= start and j <= end:
            print("*",end="")
        else:
            print(" ",end="")
    print("")