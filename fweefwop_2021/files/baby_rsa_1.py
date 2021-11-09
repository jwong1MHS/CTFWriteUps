import math

a = 643192922209641529679217093842090563198908934967463878287741

print(bytearray.fromhex(hex(a)[2:]).decode())
print(a.to_bytes(math.ceil(math.log2(a)/8), 'big'))
