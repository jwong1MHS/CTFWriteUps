var1 = "fwopCTF{this_might_be_the_flag}"
var2 = "fwopCTF{this_could_be_the_flag}"
var3 = "fwopCTF{this_potentially_is_the_flag}"
var4 = "fwopCTF{perhaps_this_is_the_flag}"
var5 = "fwopCTF{could_this_be_the_flag?}"
var6 = "fwopCTF{this_probably_isn't_the_flag}"

print("Enter the flag and I will check it for you.")
enteredFlag = input()
if enteredFlag == var4:
    print("Your flag is correct!")
else:
    print("Your flag is incorrect. :(")