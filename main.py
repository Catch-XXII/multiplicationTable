for i in range(1, 11):
    for j in range(1, 11):
        print("|{0:2d} * {1:2d} = {2:3d}".format(j, i, j*i), end=" | ")
    print("")
