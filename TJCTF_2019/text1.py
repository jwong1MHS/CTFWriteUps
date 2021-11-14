import re

mylines = []
with open('sample1.txt', 'rt') as myfile:
	for myline in myfile:
		mylines.append(myline)        

str = mylines[len(mylines) - 2]
match = re.match(r"^.*'(.*)'.*$",str)
file = open("sample2.txt","a")
file.write(match.group(1) + "\n")
file.close()






