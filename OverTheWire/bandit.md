# Bandit WarGames

Link: https://overthewire.org/wargames/bandit/

## Bandit Level 0

### Description
The goal of this level is for you to log into the game using SSH. The host to which you need \
to connect is **bandit.labs.overthewire.org**, on port 2220. The username is **bandit0** and the \
password is **bandit0**. Once logged in, go to the Level 1 page to find out how to beat Level 1.

### Solution
Open up a Linux termninal and run `ssh bandit0@bandit.labs.overthewire.org -p 2220`, which asks to remote connect to the **bandit.labs.overthewire.org** address with a username of bandit0 and at port 2220. The password to connect to the server is already given in the description.

Login: `ssh bandit0@bandit.labs.overthewire.org -p 2220` \
Password: `bandit0`

## Bandit Level 0 → Level 1

### Description
The password for the next level is stored in a file called **readme** located in the home \
directory. Use this password to log into bandit1 using SSH. Whenever you find a password \
for a level, use SSH (on port 2220) to log into that level and continue the game.

### Solution

```bash
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
Congratulations on your first steps into the bandit game!!
Please make sure you have read the rules at https://overthewire.org/rules/
If you are following a course, workshop, walkthrough or other educational activity,
please inform the instructor about the rules as well and encourage them to
contribute to the OverTheWire community so we can keep these games free!

The password you are looking for is: 
```

## Bandit Level 1 → Level 2

### Description
The password for the next level is stored in a file called **-** located in the home directory

### Solution

```bash
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat ./-

```

## Bandit Level 2 → Level 3

### Description
The password for the next level is stored in a file called **spaces in this filename** located in \
the home directory

### Solution

```bash
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat "spaces in this filename"

```

## Bandit Level 3 → Level 4

### Description
The password for the next level is stored in a hidden file in the **inhere** directory.

### Solution

```bash
bandit3@bandit:~$ ls inhere/
bandit3@bandit:~$ ls -a inhere/
.  ..  ...Hiding-From-You
bandit3@bandit:~$ cat inhere/...Hiding-From-You

```

## Bandit Level 4 → Level 5

### Description
The password for the next level is stored in the only human-readable file in the **inhere** \
directory. Tip: if your terminal is messed up, try the “reset” command.

### Solution

```bash
bandit4@bandit:~$ ls inhere/
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~$ file inhere/* | grep ASCII
inhere/-file07: ASCII text
bandit4@bandit:~$ cat inhere/-file07

```

## Bandit Level 5 → Level 6

### Description
The password for the next level is stored in a file somewhere under the **inhere** directory and \
has all of the following properties:

&emsp;&emsp;&ensp; human-readable \
&emsp;&emsp;&ensp; 1033 bytes in size \
&emsp;&emsp;&ensp; not executable

### Solution

```bash
bandit5@bandit:~$ ls inhere/
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
bandit5@bandit:~$ find . -type f -size 1033c -not -executable -exec file {} \; | grep ASCII
./inhere/maybehere07/.file2: ASCII text, with very long lines (1000)
bandit5@bandit:~$ cat inhere/maybehere07/.file2

```

## Bandit Level 6 → Level 7

### Description
The password for the next level is stored **somewhere on the server** and has all of the \
following properties:

&emsp;&emsp;&ensp; owned by user bandit7 \
&emsp;&emsp;&ensp; owned by group bandit6 \
&emsp;&emsp;&ensp; 33 bytes in size

### Solution

```bash
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password

```

## Bandit Level 7 → Level 8

### Description
The password for the next level is stored in the file **data.txt** next to the word **millionth**

### Solution

```bash
bandit7@bandit:~$ head data.txt 
momentary       MBLQ2x4SPU4Y6XIscWooXopjdSntWOhY
vicuña  6nKKKgzHbJvPFsEFQgzd2wqJWcv8TGGQ
equities        ZhOy86fNIP8sWsOLLYiHrtjRsrpu1bND
various Eg1ZcmYmpvkXS10Vu04areb2hhT9Pkft
redefinition's  vPzYXGDGwByIVBRIKQDRHn5xqoekZKME
Allison 4JPUMGRznD4JAyy1SX2Cf5zAwEhT7AP7
compels 8XgWaEyaUVmm1FLZksXE6vRBAKfm7xGB
misstep 0p0wfzDrUfyAbU6V5MVGlrvDKjmc6a0Z
coagulating     Ff0C46bfOMzwOojIDTWJAq9O59WdKSdw
Onega's YiR7TkXXHKpt0Oqs2EtFzRSXu8XGCqQA
bandit7@bandit:~$ grep millionth data.txt 
millionth       
```

## Bandit Level 8 → Level 9

### Description
The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once

### Solution

```bash
bandit8@bandit:~$ sort data.txt | uniq -u

```

## Bandit Level 9 → Level 10

### Description
The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.

### Solution

```bash
bandit9@bandit:~$ strings data.txt | grep ==
}========== the
3JprD========== passwordi
~fDV3========== is
D9========== 
```

## Bandit Level 10 → Level 11

### Description
The password for the next level is stored in the file data.txt, which contains base64 encoded data

### Solution

```bash
bandit10@bandit:~$ cat data.txt 
VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==
bandit10@bandit:~$ base64 -d data.txt 
The password is 
```

## Bandit Level 11 → Level 12

### Description
The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

### Solution

```bash
bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4
bandit11@bandit:~$ tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt
The password is 
```

## Bandit Level 12 → Level 13

### Description
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

### Solution

```bash
bandit12@bandit:/tmp/myname123$ mkdir /tmp/myname123
bandit12@bandit:/tmp/myname123$ cp data.txt /tmp/myname123
bandit12@bandit:/tmp/myname123$ cd /tmp/myname123
bandit12@bandit:/tmp/myname123$ head data.txt 
00000000: 1f8b 0808 dfcd eb66 0203 6461 7461 322e  .......f..data2.
00000010: 6269 6e00 013e 02c1 fd42 5a68 3931 4159  bin..>...BZh91AY
00000020: 2653 59ca 83b2 c100 0017 7fff dff3 f4a7  &SY.............
00000030: fc9f fefe f2f3 cffe f5ff ffdd bf7e 5bfe  .............~[.
00000040: faff dfbe 97aa 6fff f0de edf7 b001 3b56  ......o.......;V
00000050: 0400 0034 d000 0000 0069 a1a1 a000 0343  ...4.....i.....C
00000060: 4686 4341 a680 068d 1a69 a0d0 0068 d1a0  F.CA.....i...h..
00000070: 1906 1193 0433 5193 d4c6 5103 4646 9a34  .....3Q...Q.FF.4
00000080: 0000 d320 0680 0003 264d 0346 8683 d21a  ... ....&M.F....
00000090: 0686 8064 3400 0189 a683 4fd5 0190 001e  ...d4.....O.....
bandit12@bandit:/tmp/myname123$ xxd -r data.txt > data1.out
```

The pain begins here:
```bash
bandit12@bandit:/tmp/myname123$ file data1.out
data1.out: gzip compressed data, was "data2.bin", last modified: Thu Sep 19 07:08:15 2024, max compression, from Unix, original size modulo 2^32 574
bandit12@bandit:/tmp/myname123$ mv data1.out data1.gz
bandit12@bandit:/tmp/myname123$ gunzip -v data1.gz
data1.gz:        -0.9% -- replaced with data1
bandit12@bandit:/tmp/myname123$ file data1
data1: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/myname123$ mv data1 data2.bz2
bandit12@bandit:/tmp/myname123$ bunzip2 -v data2.bz2
  data2.bz2: done
bandit12@bandit:/tmp/myname123$ file data2
data2: gzip compressed data, was "data4.bin", last modified: Thu Sep 19 07:08:15 2024, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/myname123$ mv data2 data3.gz
bandit12@bandit:/tmp/myname123$ gunzip -v data3.gz
data3.gz:        98.0% -- replaced with data3
bandit12@bandit:/tmp/myname123$ file data3
data3: POSIX tar archive (GNU)
bandit12@bandit:/tmp/myname123$ mv data3 data4.tar
bandit12@bandit:/tmp/myname123$ tar -xvf data4.tar
data5.bin
bandit12@bandit:/tmp/myname123$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/myname123$ mv data5.bin data5.tar
bandit12@bandit:/tmp/myname123$ tar -xvf data5.tar
data6.bin
bandit12@bandit:/tmp/myname123$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/myname123$ mv data6.bin data6.bz2
bandit12@bandit:/tmp/myname123$ bunzip2 -v data6.bz2
  data6.bz2: done
bandit12@bandit:/tmp/myname123$ file data6
data6: POSIX tar archive (GNU)
bandit12@bandit:/tmp/myname123$ mv data6 data7.tar
bandit12@bandit:/tmp/myname123$ tar -xvf data7.tar 
data8.bin
bandit12@bandit:/tmp/myname123$ file data8.bin 
data8.bin: gzip compressed data, was "data9.bin", last modified: Thu Sep 19 07:08:15 2024, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/myname123$ mv data8.bin data8.gz
bandit12@bandit:/tmp/myname123$ gunzip -v data8.gz 
data8.gz:        -4.1% -- replaced with data8
bandit12@bandit:/tmp/myname123$ file data8
data8: ASCII text
bandit12@bandit:/tmp/myname123$ cat data8 
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```

Here is a script to do the following automatically:

```bash
#!/bin/bash

xxd -r 'data.txt' > 'data1.out'

file_number=1
file_name='data'$file_number

while true;
do
        file_name='data'$file_number
        file_data="$(file $file_name*)"
        if echo $file_data | grep 'gzip'; then
                mv $file_name* $file_name'.gz'
                gunzip -v $file_name'.gz'
                file_number=$((file_number+1))
                mv $file_name 'data'$file_number
        elif echo $file_data | grep 'bzip2'; then
                mv $file_name* $file_name'.bz2'
                bunzip2 -v $file_name'.bz2'
                file_number=$((file_number+1))
                mv $file_name 'data'$file_number
        elif echo $file_data | grep 'tar'; then
                mv $file_name* $file_name'.tar'
                tar -xvf $file_name'.tar'
                rm $file_name'.tar'
                file_number=$((file_number+1))
        elif echo $file_data | grep 'ASCII'; then
                echo "ASCII file found!"
                cat 'data'$file_number
                exit 1
        else
                echo "Unknown compression!"
                exit 1
        fi
done
```

## Bandit Level 13 → Level 14

### Description
The password for the next level is stored in **/etc/bandit_pass/bandit14 and can only be read by user bandit14**. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. **Note: localhost** is a hostname that refers to the machine you are working on

## Solution

```bash
bandit13@bandit:~$ head sshkey.private 
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAxkkOE83W2cOT7IWhFc9aPaaQmQDdgzuXCv+ppZHa++buSkN+
gg0tcr7Fw8NLGa5+Uzec2rEg0WmeevB13AIoYp0MZyETq46t+jk9puNwZwIt9XgB
ZufGtZEwWbFWw/vVLNwOXBe4UWStGRWzgPpEeSv5Tb1VjLZIBdGphTIK22Amz6Zb
ThMsiMnyJafEwJ/T8PQO3myS91vUHEuoOMAzoUID4kN0MEZ3+XahyK0HJVq68KsV
ObefXG1vvA3GAJ29kxJaqvRfgYnqZryWN7w3CHjNU4c/2Jkp+n8L0SnxaNA+WYA7
jiPyTF0is8uzMlYQ4l1Lzh/8/MpvhCQF8r22dwIDAQABAoIBAQC6dWBjhyEOzjeA
J3j/RWmap9M5zfJ/wb2bfidNpwbB8rsJ4sZIDZQ7XuIh4LfygoAQSS+bBw3RXvzE
pvJt3SmU8hIDuLsCjL1VnBY5pY7Bju8g8aR/3FyjyNAqx/TLfzlLYfOu7i9Jet67
xAh0tONG/u8FB5I3LAI2Vp6OviwvdWeC4nOxCthldpuPKNLA8rmMMVRTKQ+7T2VS
bandit13@bandit:~$ ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14

```

## Bandit Level 14 → Level 15

### Description
The password for the next level can be retrieved by submitting the password of the current level to **port 30000 on localhost**.

## Solution

```bash
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14 | nc localhost 30000
Correct!

```

## Bandit Level 15 → Level 16

## Description
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

**Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.**

## Solution

```bash
bandit15@bandit:~$ cat /etc/bandit_pass/bandit15| openssl s_client -connect localhost:30001 -ign_eof
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: E3D340C56C78BC91BBB989236F1F44E021809800B03EE5F4D88BE2881D2A39ED
    Session-ID-ctx: 
    Resumption PSK: DF878CFB8E6C7D71B779303A577C0A7E8AF8A7346348B66C425ADB3105CA4C39F49AF5FED4A87BC1ADB7F3AF28E7B86C
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - 85 69 6e 68 d9 0e 1c ff-7a 15 55 15 d2 64 36 3b   .inh....z.U..d6;
    0010 - 55 81 88 2b b7 b0 ba 2d-ca b7 70 77 8e 99 98 e4   U..+...-..pw....
    0020 - ee 35 ba 2b bf 2d f5 11-d0 64 20 a3 bc ff eb 44   .5.+.-...d ....D
    0030 - 2f a5 38 1d 54 74 b6 22-de 02 6a 8b 09 b2 69 c7   /.8.Tt."..j...i.
    0040 - c5 e2 a7 c6 0c ac 64 fd-32 71 b9 32 ab c7 03 90   ......d.2q.2....
    0050 - ad c6 07 0d 88 a1 83 fd-4f 64 0f bf 43 c0 0b 12   ........Od..C...
    0060 - ac b0 c8 00 19 4f 20 21-7a e9 c8 d0 c6 50 77 29   .....O !z....Pw)
    0070 - 3a 17 b0 d9 5c 7e e9 3e-e0 75 29 e8 15 ef 9d 30   :...\~.>.u)....0
    0080 - e3 2d ad dd 25 3e a2 44-5d 24 f2 91 0a 52 9a 06   .-..%>.D]$...R..
    0090 - 9f 1d 6b 19 bc 46 03 f0-11 bb 1a f3 47 7d b8 a0   ..k..F......G}..
    00a0 - b6 c0 17 07 43 f7 d1 24-de 2f be b1 38 49 a7 42   ....C..$./..8I.B
    00b0 - e9 e4 2b f2 27 a6 5d 16-be ee f6 34 aa 4c 8f 72   ..+.'.]....4.L.r
    00c0 - f1 f3 fc 50 bc 42 79 c3-14 fd 89 d0 1b 82 43 4d   ...P.By.......CM
    00d0 - 64 c8 f0 a9 b8 2f d5 b2-f3 b2 96 5c 58 c0 24 73   d..../.....\X.$s

    Start Time: 1738797930
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 3074EA50C94CF8001F64121107AAA1B7BAA1EC786A1AE4FCCAE464F2B1479DFA
    Session-ID-ctx: 
    Resumption PSK: 2766FF6D9F4E4A76ECB3D9D95B55B67415E741499D1740DDF8723E53AF504FA7337800FA2806BD5D76B7C06D981FBB90
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - 85 69 6e 68 d9 0e 1c ff-7a 15 55 15 d2 64 36 3b   .inh....z.U..d6;
    0010 - 8c 60 12 39 80 27 d4 68-36 15 31 16 ee 03 99 24   .`.9.'.h6.1....$
    0020 - 22 c6 0e 42 66 66 22 82-1e 09 3d a2 26 b3 57 0c   "..Bff"...=.&.W.
    0030 - 71 30 67 c6 af 43 c1 3e-c0 f3 32 20 e1 66 1d a6   q0g..C.>..2 .f..
    0040 - cc 72 d4 4c b1 87 bf 8c-8e e9 30 86 3f 56 d0 9d   .r.L......0.?V..
    0050 - 75 bf 91 da 4d 8d 57 67-c3 94 1f 0f 3c fe 72 19   u...M.Wg....<.r.
    0060 - 67 8e c1 4d c3 f1 7f d7-69 25 2a 57 73 8d 2a 31   g..M....i%*Ws.*1
    0070 - 4e 49 12 07 c5 d4 a1 75-22 a8 cf b1 dd 02 64 67   NI.....u".....dg
    0080 - 23 4a 6e 5f 35 05 32 58-3d 58 77 10 4e 01 89 4d   #Jn_5.2X=Xw.N..M
    0090 - cb 5e 3a 8c 27 c9 5e 77-9b cf a1 ef 18 18 a4 c5   .^:.'.^w........
    00a0 - 5f 02 9a dd 75 d0 8c 6a-d1 ff 9d 1b f3 27 2b 43   _...u..j.....'+C
    00b0 - a7 93 9e 7d 99 d1 32 21-e4 1e 41 30 33 90 81 10   ...}..2!..A03...
    00c0 - 5d 2d c8 f7 45 e3 18 3b-13 53 4b b9 5c 27 71 8d   ]-..E..;.SK.\'q.
    00d0 - 83 c7 e7 cf c4 79 66 64-cc 92 ba 57 54 de bc 1d   .....yfd...WT...

    Start Time: 1738797930
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
Correct!


closed
```
