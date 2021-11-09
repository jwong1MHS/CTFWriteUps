import gzip

with gzip.open('../02_Forensics/smashed.txt.gz') as f:
    string = f.read();
list(eval(string.decode('ascii')[1:-1]))
#.sort(key=lambda x:x[1])
print(string[1])
