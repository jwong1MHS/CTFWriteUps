import hashlib
import random
import re
import string

found = False
# initialize characters
while(found is False):
    first = str(random.choices(string.ascii_uppercase))
    second = str(random.choices(string.ascii_lowercase))
    third = str(random.choices(string.ascii_lowercase))
    fourth = str(random.choices(string.digits))
    fifth = '_'

# remove any brackets
    s = first + second + third + fourth + fifth
    s = re.sub('[\[\]\']', '', s)

# shuffling the characters in string
    l = list(s)
    random.shuffle(l)
    ranstr = ''.join(l)

# initializing string
    key = "tjctf{" + ranstr + "}"
    key = 'tjctf{6Vot_}'
  
# encoding GeeksforGeeks using encode() 
# then sending to md5() 
    result = hashlib.md5(key.encode()) 
  
# printing the equivalent hexadecimal value. 
    print("The hexadecimal equivalent of hash is : " + key)
    print(result.hexdigest())

    if(result.hexdigest() == '31f40dc5308fa2a311d2e2ba8955df6c'):
        print("The key is " + key)
        found = True
