import base64

string = open('../04_Crypto/ridiculous.txt', 'r').read() #base64
string = base64.b64decode(string).decode('ascii') #base64 to string
temp = ''
for i in string.split():
    temp += chr(int(i, 2))
string = temp  #bytes to base64
string = base64.b64decode(string).decode('ascii') #base64 to string
string = bytes.fromhex(string).decode('ascii') #hex to string
string = base64.b64decode(string).decode('ascii') #base64 to string

print(string)
