print("Enter the flag and I will check it for you.")
enteredFlag = input()
alphabet = "abcdefghijklmnopqrstuvwxyz{}_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
code = [5, 22, 14, 15, 31, 48, 34, 26, 0, 11, 18, 14, 28, 2, 17, 24, 15, 19, 14, 28, 11, 14, 11, 27]
correctflag = ""
for currentNum in code:
    correctflag = correctflag + alphabet[currentNum]

if enteredFlag == correctflag:
    print("Your flag is correct!")
else:
    print("Your flag is incorrect. :(")
