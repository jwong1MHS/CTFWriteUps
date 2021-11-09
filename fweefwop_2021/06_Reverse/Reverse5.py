print("Enter the flag and I will check it for you.")
enteredFlag = input()
correctflag = "deoxyribonucleic_acid"
correctflag = correctflag[0:4] + correctflag[7:16] + correctflag[5:2:-1]
correctflag = correctflag[4:-4] + correctflag[3*4:-1] + correctflag[-1:0:-2]
if enteredFlag == correctflag:
    print("Your flag is correct!")
else:
    print("Your flag is incorrect. :(")