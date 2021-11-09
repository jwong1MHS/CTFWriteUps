enteredFlag = "fwopCTF{arrays_hold_things}"
coolarray = [[[], [], []], [[], [], []], [[], [], []]]
if len(enteredFlag) == 27:
    for i in range(3):
        for j in range(3):
            for k in range(3):
              print(i, j, k)
              coolarray[i][j].append(enteredFlag[i*9 + j*3 + k])
    newflag = ""
    for i in [coolarray[2], coolarray[0], coolarray[1]]:
        for j in i[::-1]:
            for k in [j[1], j[2], j[0]]:
                newflag = newflag + k
    if newflag == "s}ginh_td{aFCTpwofolhs_yrar":
        print("Your flag is correct!")
    else:
        print("Your flag is incorrect. :(")
    print(newflag)
    print("s}ginh_td{aFCTpwofolhs_yrar")
else:
    print("Your flag is incorrect. :(")
