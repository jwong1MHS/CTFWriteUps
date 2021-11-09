print("Enter the flag and I will check it for you.")
enteredflag = input()

var1 = 15
var2 = 4
var3 = 9

if var1 < var3:
    var2 = var1 + var3
elif var3 > var2:
    var1 = (var1 * var2) - var2
else:
    var3 = var2 * var1

if var1 - var2 * var3 >= 10:
    var1 = 15 - var3
    var3 = var1 * var2
else:   
    var2 = var1 / var2
    var3 = var3 * 2


if var1 + var2 > var3:
    if var2 + 2 != var1:
        correctflag = "fwopCTF{else_elif_if_elif_else_else}"
    elif var3 - var1 >= var2 * var2:
        correctflag = "fwopCTF{else_if_then_then_else_elif}"
    elif var3 + var1 + var2 <= var3 + var1 * var2:
        correctflag = "fwopCTF{then_else_else_then_if_if}"

var3 = (var3 * -1) + var1 + var2

if var3 + var2 + var1 * 2 >= 0:
    if var3 == var2 * -2:
        correctflag = "fwopCTF{else_then_if_then_elif_elif}"
    elif var2 * var1 - var3 == 3 * var1 + 5 * var2:
        correctflag = "fwopCTF{then_if_then_else_if_if}"
    else:
        correctflag = "fwopCTF{elif_if_if_then_elif_elif}"
        
if enteredflag == correctflag:
    print("Your flag is correct!")
else:
    print("Your flag is incorrect. :(")