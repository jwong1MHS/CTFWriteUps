# OverTheWire Bandit

## Contents
- [Bandit Level 0](./bandit.md#bandit-level-0)
- [Bandit Level 0 → Level 1](./bandit.md#bandit-level-0--level-1)
- [Bandit Level 1 → Level 2](./bandit.md#bandit-level-1--level-2)
- [Bandit Level 2 → Level 3](./bandit.md#bandit-level-2--level-3)
- [Bandit Level 3 → Level 4](./bandit.md#bandit-level-3--level-4)
- [Bandit Level 4 → Level 5](./bandit.md#bandit-level-4--level-5)
- [Bandit Level 5 → Level 6](./bandit.md#bandit-level-5--level-6)
- [Bandit Level 6 → Level 7](./bandit.md#bandit-level-6--level-7)
- [Bandit Level 7 → Level 8](./bandit.md#bandit-level-7--level-8)
- [Bandit Level 8 → Level 9](./bandit.md#bandit-level-8--level-9)
- [Bandit Level 9 → Level 10](./bandit.md#bandit-level-9--level-10)
- [Bandit Level 10 → Level 11](./bandit.md#bandit-level-10--level-11)
- [Bandit Level 11 → Level 12](./bandit.md#bandit-level-11--level-12)
- [Bandit Level 12 → Level 13](./bandit.md#bandit-level-12--level-13)

***

## Bandit Level 0

### Description
The goal of this level is for you to log into the game using SSH. The host to which you need \
to connect is **bandit.labs.overthewire.org**, on port 2220. The username is **bandit0** and the \
password is **bandit0**. Once logged in, go to the Level 1 page to find out how to beat Level 1.

Link: https://overthewire.org/wargames/bandit/bandit0.html

### Write Up
Open up a Linux termninal and run `ssh bandit0@bandit.labs.overthewire.org -p 2220`, which asks to remote connect to the **bandit.labs.overthewire.org** address with a username of bandit0 and at port 2220. The password to connect to the server is already given in the description.

Login: `ssh bandit0@bandit.labs.overthewire.org -p 2220` \
Password: `bandit0`

***

## Bandit Level 0 → Level 1

### Description
The password for the next level is stored in a file called **readme** located in the home \
directory. Use this password to log into bandit1 using SSH. Whenever you find a password \
for a level, use SSH (on port 2220) to log into that level and continue the game.

Link: https://overthewire.org/wargames/bandit/bandit1.html

### Write Up
While logged into bandit0, run `ls` to list all the files in the current directory. It shows that there is a file in the directory called **readme**. To read the file, run `cat readme` which prints the contents of the file onto the console. The password is the content that is printed out.

    bandit0@bandit:~$ ls
    readme
    bandit0@bandit:~$ cat readme
    boJ9jbbUNNfktd78OOpsqOltutMc3MY1

Login: `ssh bandit1@bandit.labs.overthewire.org -p 2220` \
Password: `boJ9jbbUNNfktd78OOpsqOltutMc3MY1`

***

## Bandit Level 1 → Level 2

### Description
The password for the next level is stored in a file called **-** located in the home directory

Link: https://overthewire.org/wargames/bandit/bandit2.html

### Write Up
Run `ls`, and there should be a file called **-** in the system. Trying to run `cat -` will cause the terminal to freeze, because the **-** character is also a characters used for flags. Instead, to output a file with special characters, an alternative is to point to the point to the current directory by adding **./** . Run `cat ./-`.

    bandit1@bandit:~$ ls
    -
    bandit1@bandit:~$ cat ./-
    CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

Login: `ssh bandit2@bandit.labs.overthewire.org -p 2220` \
Password: `CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9`

***

## Bandit Level 2 → Level 3

### Description
The password for the next level is stored in a file called **spaces in this filename** located in the home directory

Link: https://overthewire.org/wargames/bandit/bandit3.html

### Write Up
Run `ls`, and there should be a file in the current directory. Trying to run `cat spaces in this filename` will give errors such as: 

    bandit2@bandit:~$ cat spaces in this filename
    cat: spaces: No such file or directory
    cat: in: No such file or directory
    cat: this: No such file or directory
    cat: filename: No such file or directory

The terminal treats every string as a file argument for cat. To run a file with spaces in the name, surround the file name with double quotations (""). Running `cat "spaces in this filename"` will print the contents of that file.

Note: just typing `cat s` and then pressing <kbd>Tab</kbd> will autocomplete the file name since it is the only file in the system that starts with an s.

P.S. Never name a file with spaces in it, generally files are named as **spacesinthisfilename** or **spacesInThisFilename** or **spaces_in_this_filename** for example.

    bandit2@bandit:~$ ls
    spaces in this filename
    bandit2@bandit:~$ cat "spaces in this filename" 
    UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

Login: `ssh bandit3@bandit.labs.overthewire.org -p 2220` <br>
Password: `UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK`

***

## Bandit Level 3 → Level 4

### Description
The password for the next level is stored in a hidden file in the **inhere** directory.

Link: https://overthewire.org/wargames/bandit/bandit4.html

### Write Up
Running `ls` will show that there is a directory called **inhere** in the current directory (the directory text is in blue compared to the white text for files, and you can also check by running `file inhere` which shows that it's a directory). To change the current directory to the **inhere** directory, run `cd inhere`. 

Running another `ls` in that directory will show that there are no files in the directory. However, running ls with the -a flag (`ls -a`) will show that there is a hidden file called **.hidden**, which is indicated by the . before the filename. Printing the file using `cat .hidden` will give the password string. 

Note: `cd` is short of change directory

    bandit3@bandit:~$ ls
    inhere
    bandit3@bandit:~$ cd inhere/
    bandit3@bandit:~/inhere$ ls
    bandit3@bandit:~/inhere$ ls -a
    .  ..  .hidden
    bandit3@bandit:~/inhere$ cat ./.hidden 
    pIwrPrtPN36QITSp3EQaw936yaFoFgAB

Login: `ssh bandit4@bandit.labs.overthewire.org -p 2220` \
Password: `pIwrPrtPN36QITSp3EQaw936yaFoFgAB`

***

## Bandit Level 4 → Level 5

### Description
The password for the next level is stored in the only human-readable file in the **inhere** \
directory. Tip: if your terminal is messed up, try the “reset” command.

Link: https://overthewire.org/wargames/bandit/bandit5.html

### #Write Up
Change directory into the **inhere** directory and run an `ls`, which will show that there are 10 files in the directory. To find the file type of each file, use the `file` command. Attempting to run `file -file00` will produce the following error:

    bandit4@bandit:~/inhere$ file -file00
    file: Cannot open `ile00' (No such file or directory).

The - at the beginning of the filename makes the file command treat the -f in the filename as a flag, and the rest of the filename string as the file we're working with, which does not exist.

Doing `file ./-file00` on the first file will produce a result, and it shows that the file type is of type **data**, which is not human-readable. To check the file type of every file in the directory, run `file ./-file0*`, which will run every file that starts with "-file0".

Only **-file07** is an ASCII text file type which is human-readable, so a simple `cat ./-file07` will give the password.

    bandit4@bandit:~$ cd inhere
    bandit4@bandit:~/inhere$ ls
    -file00  -file02  -file04  -file06  -file08
    -file01  -file03  -file05  -file07  -file09
    bandit4@bandit:~/inhere$ file ./-file00
    ./-file00: data
    bandit4@bandit:~/inhere$ file ./-file0*
    ./-file00: data
    ./-file01: data
    ./-file02: data
    ./-file03: data
    ./-file04: data
    ./-file05: data
    ./-file06: data
    ./-file07: ASCII text
    ./-file08: data
    ./-file09: data
    bandit4@bandit:~/inhere$ cat ./-file07
    koReBOKuIDDepwhWk7jZC0RTdopnAYKh

Login: `ssh bandit5@bandit.labs.overthewire.org -p 2220` \
Password: `koReBOKuIDDepwhWk7jZC0RTdopnAYKh`

***

## Bandit Level 5 → Level 6

### Description
The password for the next level is stored in a file somewhere under the **inhere** directory and \
has all of the following properties:

&emsp;&emsp;&ensp; human-readable \
&emsp;&emsp;&ensp; 1033 bytes in size \
&emsp;&emsp;&ensp; not executable

Link: https://overthewire.org/wargames/bandit/bandit6.html

### Write Up
Change directory into the **inhere** directory and run an `ls`, which will show that there are 18 directories directories. Rather than iterating through each directory and checking the size of every item in the directory with an `ls -l`, we can find all the files in the directory that matches the 1033 byte size by doing `find . -size 1033c`, which finds every file in the directory and only grabs those of the specified size.

We see that the **./maybehere07/.file2** file is the only one that matches the size, so a simple `cat ./maybehere07/.file2` gives us the password.

    bandit5@bandit:~$ cd inhere/
    bandit5@bandit:~/inhere$ ls
    maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
    maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
    maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
    bandit5@bandit:~/inhere$ find . -size 1033c
    ./maybehere07/.file2
    bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
    DXjZPULLxYr17uwoI01bNLQbtFemEgo7

Login: `ssh bandit6@bandit.labs.overthewire.org -p 2220` \
Password: `DXjZPULLxYr17uwoI01bNLQbtFemEgo7`

***

## Bandit Level 6 → Level 7

### Description
The password for the next level is stored **somewhere on the server** and has all of the \
following properties:

&emsp;&emsp;&ensp; owned by user bandit7 \
&emsp;&emsp;&ensp; owned by group bandit6 \
&emsp;&emsp;&ensp; 33 bytes in size

Link: https://overthewire.org/wargames/bandit/bandit7.html

### Write Up
Since the file that we are looking for is somewhere on the server, that means it's not guaranteed to be in the current working directory, so it is somewhere in the root directory (you can `cd /` to see the contents of the root directory). Instead of going through every file in the root directory (because there are a lot of files in root), we can use the `find` command and pass in all the flags we need such as `find / -user bandit7 -group bandit6 -size 33c`, which checks under the root directory for any file that fits those criteria.

The location of the file is printed out, but a lot of permission denied statements are also printed onto the console, because those are the error messages produced when the `file` command iteriated through every file in the filesystem. A clean way to remove those error messages is to do `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`.

We see that the **/var/lib/dpkg/info/bandit7.password** file is the only one that matches the size, so a simple `cat ./maybehere07/.file2` gives us the password.

    bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
    /var/lib/dpkg/info/bandit7.password
    bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
    HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

Login: `ssh bandit7@bandit.labs.overthewire.org -p 2220` \
Password: `HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs`

***

## Bandit Level 7 → Level 8

### Description
The password for the next level is stored in the file **data.txt** next to the word **millionth**

Link: https://overthewire.org/wargames/bandit/bandit8.html

### Write Up
A quick `ls` shows that the file **data.txt** is in the current directory. However, trying to run `cat data.txt` will print a lot of text from **data.txt** onto the console, and it's inefficient to manually look for the word **millionth**. Instead, run `cat data.txt | grep millionth`, which will take the output of `cat` and pipe (|) it into grep (a command that looks for a string in a file). The password is next to the word **millionth**.

    bandit7@bandit:~$ grep millionth data.txt
    millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV

Login: `ssh bandit8@bandit.labs.overthewire.org -p 2220` \
Password: `cvX2JJa4CFALtqS87jk27qwqGhBM9plV`

***

## Bandit Level 8 → Level 9

### Description
The password for the next level is stored in the file **data.txt** and is the only line of text that \
occurs only once

Link: https://overthewire.org/wargames/bandit/bandit9.html

### Write Up
A quick `cat` on the **data.txt** file shows a lot of text, and the goal is to get the only line of text that is unique. One command that would be useful to use is `uniq`, but doing `uniq data.txt` will still give a lot of text. This is because `uniq` only filters out duplicates, so if we want to grab only unique lines use the `-u` flag. Also, `uniq` only checks adjacent lines for duplicates, so to find one occurence within a file all the lines should be sorted first before doing a `uniq`. Executing `sort data.txt | uniq -u` will give us the one unique line.

    bandit8@bandit:~$ sort data.txt | uniq -u
    UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

Login: `ssh bandit9@bandit.labs.overthewire.org -p 2220` \
Password: `UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR`

***

## Bandit Level 9 → Level 10

### Description
The password for the next level is stored in the file **data.txt** in one of the few human-\
readable strings, preceded by several ‘=’ characters.

Link: https://overthewire.org/wargames/bandit/bandit10.html

### Write Up
Running `cat` on **data.txt** will show a lot of gibberish, which most likely means that the file is not an ASCII file. Running `file data.txt` shows that it is instead a data/binary file, so instead use `strings` on the file. Running `strings data.txt` will give more readable characters, and to get all the lines that have several '=' characters, running `strings data.txt | grep -i ==` will do the trick, since there will be at least 2 '=' characters in each line. Note that attempting to run `grep -i == data.txt` will just return `Binary file data.txt matches` because grep does not work on binary files.

    bandit9@bandit:~$ strings data.txt | grep -i ==
    ========== the*2i"4
    ========== password
    Z)========== is
    &========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

Login: `ssh bandit10@bandit.labs.overthewire.org -p 2220` \
Password: `truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk`

***

## Bandit Level 10 → Level 11

### Description
The password for the next level is stored in the file data.txt, which contains base64 \
encoded data

Link: https://overthewire.org/wargames/bandit/bandit11.html

### Write Up
Running `cat` on **data.txt** will show some text, but it is base64 encoded because of the character at the end of the string. Rather than copying and pasting the string into an online base64 decoder, running `base64 -d data.txt` will decode the contents of the file and output it onto the console.

    bandit10@bandit:~$ cat data.txt
    VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==
    bandit10@bandit:~$ base64 -d data.txt
    The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

Login: `ssh bandit11@bandit.labs.overthewire.org -p 2220` \
Password: `IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR`

***

## Bandit Level 11 → Level 12

### Description
The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and \
uppercase (A-Z) letters have been rotated by 13 positions

Link: https://overthewire.org/wargames/bandit/bandit12.html

### Write Up
Running `cat` on **data.txt** will show letters but they've all been shifted.  Rather than copying and pasting the string into an online ROT13 cipher, running `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'` will decode the contents of the file and output it onto the console. What `tr` does is translate/delete characters, so `tr 'A-Z' 'N-ZA-M'` maps A's to N's, B's to O, ..., N's to A's, etc, and we want to do the same for lowercase letters as well. It maps the 52 characters to another set of 52 characters.

    bandit11@bandit:~$ cat data.txt
    Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh
    bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
    The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

Login: `ssh bandit12@bandit.labs.overthewire.org -p 2220` \
Password: `5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu`

***

## Bandit Level 12 → Level 13

### Description
The password for the next level is stored in the file data.txt, which is a hexdump of a file \
that has been repeatedly compressed. For this level it may be useful to create a directory \
under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then \
copy the datafile using cp, and rename it using mv (read the manpages!)

Link: https://overthewire.org/wargames/bandit/bandit13.html

### Write Up
