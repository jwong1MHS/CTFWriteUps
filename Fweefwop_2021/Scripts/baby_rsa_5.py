import sympy

p = 194522226411154500868209046072773892801
q = 288543888189520095825105581859098503663
e = 65537

n = p*q
totient = sympy.totient(n)
d = sympy.mod_inverse(e, totient)
print(d)
