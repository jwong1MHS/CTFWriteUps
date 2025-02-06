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

### Solution

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

### Solution

```bash
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14 | nc localhost 30000
Correct!

```

## Bandit Level 15 → Level 16

### Description
The password for the next level can be retrieved by submitting the password of the current level to **port 30001** on localhost using SSL/TLS encryption.

**Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.**

### Solution

```bash
bandit15@bandit:~$ cat /etc/bandit_pass/bandit15 | openssl s_client -connect localhost:30001 -ign_eof
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

## Bandit Level 16 → Level 17

### Description
The credentials for the next level can be retrieved by submitting the password of the current level to **a port on localhost in the range 31000 to 32000**. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

**Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.**

### Solution

```bash
bandit16@bandit:~$ nmap localhost -p 31000-32000 --script ssl-cert
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-02-06 00:05 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00012s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
| ssl-cert: Subject: commonName=SnakeOil
| Issuer: commonName=SnakeOil
| Public Key type: rsa
| Public Key bits: 4096
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-06-10T03:59:50
| Not valid after:  2034-06-08T03:59:50
| MD5:   fa04:c746:b0d0:c3a1:984c:0708:ed4c:4505
|_SHA-1: 323a:f3b1:4fc7:1b0f:f71a:1931:8ff3:62a1:49ac:735a
31691/tcp open  unknown
31790/tcp open  unknown
| ssl-cert: Subject: commonName=SnakeOil
| Issuer: commonName=SnakeOil
| Public Key type: rsa
| Public Key bits: 4096
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-06-10T03:59:50
| Not valid after:  2034-06-08T03:59:50
| MD5:   fa04:c746:b0d0:c3a1:984c:0708:ed4c:4505
|_SHA-1: 323a:f3b1:4fc7:1b0f:f71a:1931:8ff3:62a1:49ac:735a
31960/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.37 seconds
```

```bash
bandit16@bandit:~$ cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31790 -ign_eof
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
    Session-ID: 0195048859E8694A69BD8962482CEAAA6F82A4C744EF509649D8589656158539
    Session-ID-ctx: 
    Resumption PSK: 36D68B13807BAD6316067A4BB47AACB6BCD3D7985797305F80FBC83986C32F63AC54878917F4B421BCCB3637CA1C859F
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - fa 2c 20 00 e8 02 f6 8f-7c 28 09 bb ff 4b 33 cd   ., .....|(...K3.
    0010 - e6 1d b0 19 51 d4 95 56-5b 0b b9 d7 85 d3 85 6f   ....Q..V[......o
    0020 - 59 29 da 40 68 9a 61 b0-1c 21 e3 fe cf 4c 11 ba   Y).@h.a..!...L..
    0030 - 33 50 f9 16 72 1a 7d 82-f7 18 bc b4 80 7e ba 11   3P..r.}......~..
    0040 - 59 5d 4f 55 37 1b 44 ae-9f d0 f3 e7 93 0f 9a 94   Y]OU7.D.........
    0050 - 1b d3 1b 88 e9 f5 83 c7-0d 45 03 b2 d4 3d ae 64   .........E...=.d
    0060 - e9 1d 0d 60 90 15 25 30-c7 5d 96 de 16 88 68 e4   ...`..%0.]....h.
    0070 - c6 06 91 7d 95 1f 08 60-02 a4 9c 27 09 1c f0 2a   ...}...`...'...*
    0080 - eb ca 04 ce 2a 1e 2e f5-a8 7a 04 f6 2f c0 ee df   ....*....z../...
    0090 - d7 f4 3c 65 a7 7a a9 b5-17 d5 4c ca 3c 65 01 74   ..<e.z....L.<e.t
    00a0 - 59 68 a2 a2 ec c2 39 32-73 3d 80 95 f5 f0 95 10   Yh....92s=......
    00b0 - 9b df c0 9b 48 16 f7 a9-78 64 3b de 5f 78 e4 20   ....H...xd;._x. 
    00c0 - 91 29 54 1b 96 66 6d d9-3c 80 47 1e 45 29 b3 c7   .)T..fm.<.G.E)..
    00d0 - 6a 3f 71 a0 30 03 05 45-95 90 22 2f c7 1f c7 18   j?q.0..E.."/....

    Start Time: 1738800579
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
    Session-ID: 2780A75EBFA9F5DD64622404485785376BC9DA5420090E502C6AC8F97D3E6BB7
    Session-ID-ctx: 
    Resumption PSK: A15FD2BC589B4F4F3338F6AEDCE5028923B0CA66546AEA511003C2FC737F4C71029DC4EA585DB64EFF0F63EF84904065
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - fa 2c 20 00 e8 02 f6 8f-7c 28 09 bb ff 4b 33 cd   ., .....|(...K3.
    0010 - e7 d5 97 07 5d 36 f7 c2-d6 e5 5f 98 3f fc 46 92   ....]6...._.?.F.
    0020 - a5 4f 10 0c 5d e2 72 90-56 91 40 7d 9b 46 c3 29   .O..].r.V.@}.F.)
    0030 - 18 3b b9 f3 dc 9c 6f 54-00 d1 36 2c aa 13 5a 4e   .;....oT..6,..ZN
    0040 - d8 04 29 7d 82 91 10 61-05 df 68 9c fc c2 5b 7c   ..)}...a..h...[|
    0050 - 89 e4 92 02 85 0b 21 d7-51 52 e1 65 99 eb 31 32   ......!.QR.e..12
    0060 - d3 cb 50 e1 48 a2 4b f8-8b 37 e2 86 8f 7d 2d 3e   ..P.H.K..7...}->
    0070 - b2 8e f6 84 fb 4a 86 52-c4 a4 3a 0c a2 fb 16 c4   .....J.R..:.....
    0080 - 67 d8 a2 40 c7 d3 90 7e-ec b1 89 f2 c6 a3 8d 17   g..@...~........
    0090 - 5c 21 85 6f 03 06 e5 86-27 0a 03 38 be 38 0d 57   \!.o....'..8.8.W
    00a0 - bc 3e 67 13 1d c4 a0 7a-a0 85 83 cc 59 ed 15 be   .>g....z....Y...
    00b0 - 6d 91 00 c1 88 ea 17 ca-6b 70 1f f0 2b ba 40 a8   m.......kp..+.@.
    00c0 - 11 03 1f 0e 37 3e 80 48-6c 9f 33 68 78 cb 44 bf   ....7>.Hl.3hx.D.
    00d0 - 76 66 ce e1 12 0b e7 b1-64 f0 55 84 57 0f 44 d5   vf......d.U.W.D.

    Start Time: 1738800579
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
```

```bash
bandit16@bandit:~$ cd $(mktemp -d)
bandit16@bandit:/tmp/tmp.CoPIgO1USU$ echo "-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----" > sshkey.private
bandit16@bandit:/tmp/tmp.CoPIgO1USU$ chmod go-rwx sshkey.private
bandit16@bandit:/tmp/tmp.CoPIgO1USU$ ssh -i sshkey.private bandit17@bandit.labs.overthewire.org -p 2220
bandit17@bandit:~$ cat /etc/bandit_pass/bandit17

```

## Bandit Level 17 → Level 18

### Description
There are 2 files in the homedirectory: **passwords.old and passwords.new**. The password for the next level is in **passwords.new** and is the only line that has been changed between **passwords.old and passwords.new**

**NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19**

### Solution

```bash
bandit17@bandit:~$ diff passwords.new passwords.old 
42c42
< x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
---
> ktfgBvpMzWKR5ENj26IbLGSblgUG9CzB
```

## Bandit Level 18 → Level 19

### Description
The password for the next level is stored in a file **readme** in the homedirectory. Unfortunately, someone has modified **.bashrc** to log you out when you log in with SSH.

### Solution

```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
```

## Bandit Level 19 → Level 20

### Description
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

### Solution

We can use the script to execute commands as the `bandit20` user.

```bash
bandit19@bandit:~$ ./bandit20-do id
uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```
