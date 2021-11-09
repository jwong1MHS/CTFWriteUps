key = "fwopCTF{I_am_learning_RSA_so_exciting}"
flag = 0

for i in range(len(key)):
    flag = flag*({True: 1, False: 256}[i==0]) + ord(key[i])

print(flag)
