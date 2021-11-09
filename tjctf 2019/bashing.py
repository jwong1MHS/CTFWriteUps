import hashlib
import random
import re
import string

found = False
while(found is False):
    first = str(random.choices(string.ascii_uppercase))
    second = str(random.choices(string.ascii_lowercase))
    third = str(random.choices(string.ascii_lowercase))
    fourth = str(random.choices(string.digits))

    s = first + second + third + fourth + '_'
    s = re.sub('[\[\]\']', '', s)

    l = list(s)
    random.shuffle(l)
    ranstr = ''.join(l)

    key = "tjctf{" + ranstr + "}"
  
    result = hashlib.md5(key.encode()) 

    if(result.hexdigest() == '31f40dc5308fa2a311d2e2ba8955df6c'):
        print("The key is " + key)
        found = True
