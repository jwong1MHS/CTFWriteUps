p = 194522226411154500868209046072773892801
q = 288543888189520095825105581859098503663
e = 65537
N = 'fwop{baby_rsa}'

n = p*q
byte = bytes(N, 'ascii')
m = int.from_bytes(byte, 'big')
c = pow(m, e, n)

print(c)
