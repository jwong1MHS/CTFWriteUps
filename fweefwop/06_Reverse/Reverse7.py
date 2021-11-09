print("Enter the flag and I will check it for you.")
enteredFlag = input()

semicolonpos = 0
fail = False
if len(enteredFlag) != 20:
    print("Your flag is incorrect. :(")
else:
    enteredFlag = enteredFlag[12:20] + enteredFlag[0:12]
    for i in range(20):
        if enteredFlag[i] == ";":
            semicolonpos = i
        elif enteredFlag[i] == "q":
            break;
    else:
        fail = True
    if not fail:
        enteredFlag = enteredFlag[0:semicolonpos] + "o_dddduel}"
    if enteredFlag == "fwopCTF{its_time_to_dddduel}":
        print("Your flag is correct!")
    else:
        print("Your flag is incorrect. :(")