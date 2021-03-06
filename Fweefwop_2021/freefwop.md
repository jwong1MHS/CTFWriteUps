Link: https://ctf.fweefwop.club/challenges

## 01 General
|             Challenge             |              Flag              |                             Method                             |
| --------------------------------- | ------------------------------ | -------------------------------------------------------------- |
| Assembly Warm Up (100)            | fwopCTF{Assembly}              | Google/Common Knowledge                                        |
| Base2 (100)                       | fwopCTF{11101000}              | [Hex to Decimal](https://www.rapidtables.com/convert/number/hex-to-decimal.html) |
| Base64 Abridged (100)             | fwopCTF{SSBsb3ZlIENURg==}      | [ASCII to Base64](https://gchq.github.io/CyberChef/#recipe=To_Base64('A-Za-z0-9%2B/%3D')) |
| Hex the way in (100)              | fwopCTF{back_from_hex}         | [Hex to ASCII](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')) |
| Jon Us in Discord (100)           | fwopCTF{fweefwop_ctf_go_go_go} | [Discord Link](https://discord.gg/y2BXfQCgmN)                  |
| Name this language (6) (100)      | fwopCTF{BASIC}                 | Google                                                         |
| Touch the base (100)              | fwopCTF{base64_is_everywhere}  | [Base64 to ASCII](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)) |
| Warm Up -- Let's Start! (100)     | fwopCTF{this_is_the_flag}      | Copy/paste                                                     |
| Zeros and Ones (100)              | fwopCTF{complicated}           | [Binary to ASCII](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)) |
| Assembly: MOV and ADD (150)       | fwopCTF{37223}                 | [Assembly Emulator](https://carlosrafaelgn.com.br/Asm86)       |
| Assembly: Reset a register (150)  | fwopCTF{xor}                   | [Assembly Emulator](https://carlosrafaelgn.com.br/Asm86)       |
| Assembly: Stack (1) (150)         | fwopCTF{0x123}                 | [Assembly Emulator](https://carlosrafaelgn.com.br/Asm86)       |
| Assembly: Stack (2) (150)         | fwopCTF{0x123}                 | [Assembly Emulator](https://carlosrafaelgn.com.br/Asm86)       |
| Modular (3) (150)                 | fwopCTF{3500}                  | [WolframAlpha](https://www.wolframalpha.com/input/?i=5%5Ep+mod+7001%3D1) |
| MOV again (150)                   | fwopCTF{8738}                  | [Assembly Emulator](https://carlosrafaelgn.com.br/Asm86)       |
| Name this language (1) (150)      | fwopCTF{Rust}                  | Google                                                         |
| Name this language (2) (150)      | fwopCTF{Go}                    | Google                                                         |
| Name this language (3) (150)      | fwopCTF{Fortran}               | Google                                                         |
| Name this language (4) (150)      | fwopCTF{COBOL}                 | Google                                                         |
| Name this language (5) (150)      | fwopCTF{Lisp}                  | Google                                                         |
| Name this language (7) (150)      | fwopCTF{Prolog}                | Google                                                         |
| Name this language (8) (150)      | fwopCTF{Haskell}               | Google                                                         |
| Name this language(0) (150)       | fwopCTF{C}                     | Google                                                         |
| Shift (150)                       | fwopCTF{0x1200}                | [Assembly Emulator](https://carlosrafaelgn.com.br/Asm86)       |
| What is that thing? (3) (150)     | fwopCTF{icmp}             | [Common Protocols](https://en.wikibooks.org/wiki/Network_Plus_Certification/Technologies/Common_Protocols) |
| What's that thing? (0) (150)      | fwopCTF{compiler}              | Common Knowledge                                               |
| What's that thing? (1) (150)      | fwopCTF{daemon}                | Google                                                         |
| What's that thing? (2) (150)      | fwopCTF{switch}                | [Types of Network Devices](https://www.educba.com/types-of-network-devices/) |
| Modular (0) (200)                 | fwopCTF{4}                     | Wolframalpha/Mental math                                       |
| Modular (1) (200)                 | fwopCTF{31}                    | [WolframAlpha](https://www.wolframalpha.com/input/?i=x+*+11+%3D+46+%28mod+59%29) |
| Modular (2) (200)                 | fwopCTF{194}                   | [WolframAlpha](https://www.wolframalpha.com/input/?i=x*x+%3D+2+%28mod+607%29) |
| NASM (2) (200)                    | fwopCTF{9}                     | Line 13 of hello.asm                                           |
| XOR warm up (200)              | fwopCTF{xor_rules} | [XOR with key 01](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Hex','string':'01'%7D,'Standard',false)) |
| NASM (1) (250)                    | fwopCTF{i_have_done_this_ex}   | [Online NASM Emulator](https://rextester.com/l/nasm_online_compiler)  |
| Go through some gates (300)       | fwopCTF{1}                     | [Digital Logic](https://www.circuitbasics.com/what-is-digital-logic/) |
| Assembly: Jump (400)              | fwopCTF{fwop}                  | Line 33 from 0x0? to 0x0d                                      |
| Modular (4) (400)                 | fwopCTF{278505}                | `pow(31, pow(31, 2813771283, totient(384302)), 384302)`        |

## 02 Forensics
|              Challenge              |                Flag                |                                Method                                |
| ----------------------------------- | ---------------------------------- | -------------------------------------------------------------------- |
| Alice in Wonderland? (100)          | fwopCTF{Beneath_the_surface}       | `strings garden.jpg`                                                 |
| Just inflate me (100)               | fwopCTF{ok_you_found_me}           | `gunzip flag.txt.gz`                                                 |
| Not Viewable (100)                  | fwopCTF{actually_an_image}         | change `fflag.txt` to .png or .jpg                                   |
| The Meta Joke (100)                 | fwopCTF{metadata_is_funky}         | [Metadata Viewer](http://exif.regex.info/exif.cgi) `file MyCoolCard.jpg` |
| Not the same (150)                  | fwopCTF{r3sp3ct_th3_d1ff}          | `diff t1.txt t2.txt`                                                 |
| Reading between the Eyes (150)      | fwopCTF{r34d1ng_b37w33n_7h3_by73s} | [Steganography Online](https://stylesuxx.github.io/steganography/)   |
| Sharper Image (150)                 | fwopCTF{this_is_a_boring_flag}     | `base64 -d bb.txt  > bb.png`                                         |
| Bitcoin Laundering (0) (200)        | fwopCTF{20000}                     | <code>grep -o -i { transactions.json &#124; wc -l</code>  |
| Follow the Shiba (200)           | fwopCTF{steg_is_fun} | [Steganography Online](https://stylesuxx.github.io/steganography/) Check LSB of first file, grab imgur link, LSB |
| Pranked (200)                       | fwopCTF{easilypranked}             | Inspect element, https://tinyurl.com/easilypranked                   |
| What is in this Cookie? (200)       | fwopCTF{ThisIsSoMuchFun}           | [Steganography Online](https://stylesuxx.github.io/steganography/)   |
| What's inside of this apple? (200)  |                                    |                                                                      |
| Wood Door (250)                     | fwopCTF{hiding_in_bit_plane}       | [StegOnline](https://stegonline.georgeom.net/) Blue 2                |
| Apples & Oranges (250)     | fwopCTF{which_is_your_favorite}    | [Steganographic Decoder](https://futureboy.us/stegano/decinput.html) or `steghide extract -sf Apple.jpg` |
| Corrupted_File (300)                | fwopCTF{C0rrupted}        | Make sure the first 18 and last 12 bytes of a PNG match w. Hexedit `89 50 4E 47 0D 0A 1A 0A 00 00 00 0D` |
| Kevin zzZZ (400)                    | fwopCTF{rick_fan_are_you_not?}     | `binwalk --dd=".*" kevin_zzZZ.jpg`, `file *`, `mv 21FB71 21FB71.png`, Scan QR code |


## 03 Linux Lab
|             Challenge             |                Flag                |                               Method                               |
| --------------------------------- | ---------------------------------- | ------------------------------------------------------------------ |
| Linux Lab Level 1 (100)           | fwopCTF{level_1_u3xe4}             | `ssh level0@linux.fweefwop.club`, Password: fwopCTF{level_0}, `ls` |
| Linux Lab Level 2 (100)           | fwopCTF{level_2_l46h3}             | `cd subdir`, `ls`                                                  |
| Linux Lab Level 3 (100)           | fwopCTF{level_3_ti8fx}             | `cat flag.txt`                                                     |
| Linux Lab Level 4 (100)           | fwopCTF{level_4_nmc4e}             | `env`                                                              |
| Linux Lab Level 5 (100)           | fwopCTF{level_5_4gw}               | A lot of `ls` and `cd` and autocomplete with <kbd>Tab</kbd>        |
| Linux Lab Level 6 (100)           | fwopCTF{level_6_3bw}               | <code>cat flag.txt &#124; grep -i fwopCTF{</code>                  |
| Linux Lab Level 7 (100)           | fwopCTF{level_7_82j}               | `cat .flag.txt`                                                    |
| Linux Lab Level 8 (100)           | fwopCTF{level_8_2b3}               | `cat flag.png`                                                     |
| Linux Lab Level 9 (100)           | fwopCTF{level_9_c2p}               | `diff f1.txt f2.txt`                                               |
| Linux Lab Level 10 (100)          | fwopCTF{level_10_fqd}              | `cat ./-cant_touch_this`                                           |
| Linux Lab Level 11 (100)          | fwopCTF{level_11_87h}              | `cat readme` --> `find / -name level11_flag.txt 2> /dev/null`      |

## 04 Crypto
|             Challenge             |                       Flag                       |                               Method                               |
| --------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------ |
| Baby RSA (2) (100)                | 56128199547956677238767298622332803823913995062683233044001500290070667830063 | `python3 baby_rsa_2`                  |
| Baby RSA (3) (100)                | 56128199547956677238767298622332803823430928948082558447308185662138795433600 | `python3 baby_rsa_3`                  |
| Caesar (100)                      | fwopCTF{Brutus_says_Ceaser_sucks}                | [Ceasar cipher](https://www.dcode.fr/caesar-cipher) shift 16       |
| FlipFwop (100)                    | fwopCTF{earth_fire_water_air}                    | [Flip](http://flipapicture.com/) flip horizontally                 |
| Oink (100)                        | fwopCTF{welovepigs}                              | [Pigpen cipher](https://en.wikipedia.org/wiki/Pigpen_cipher)       |
| Simple MD5 (100)                  | fwopCTF{7ca2197c58b026825c382e32621b1ce4}        | [MD5](https://gchq.github.io/CyberChef/#recipe=MD5())              |
| Some Ciphers (100)                | fwopCTF{multi_cipher_shenanigans}           | [ROT13](https://rot13.com/), [Caesar cipher](https://www.dcode.fr/caesar-cipher) shift 3 | | Where's the message? (100)        | fwopCTF{WOWTHANKS}                               | Read the first letter of each work on each line                    |
| WireBirds (100)                   | fwopCTF{BIRDSKNOW}                               | [Birds on a Wire Cipher](https://www.dcode.fr/birds-on-a-wire-cipher) |
| More than 64 (125)                | fwopCTF{other_bases_would_work_too_not_just_64}  | [Cipher Identifier](https://www.dcode.fr/cipher-identifier), [Base85](https://gchq.github.io/CyberChef/#recipe=From_Base85('!-u')) |
| Baby RSA (1) (150)                | fwopCTF{another_baby_rsa}                        | `python3 baby_rsa_1` |
| ROT More (150)                    | fwopCTF{r0t47_t_is}                              | [ROT47](https://gchq.github.io/CyberChef/#recipe=ROT47(47))        |
| Samuel Morse (150)                | fwopCTF{MORSE_CODE_EASY}               | [Morse Code](https://gchq.github.io/CyberChef/#recipe=From_Morse_Code('Space','Line%20feed')) |
| 5x5  (200)                        | fwopCTF{POLYBIUSSQUARE}                        | [Polybius Cipher](https://www.dcode.fr/polybius-cipher) key=ABCDEFGHIKLMNOPQRSTUVWXYZ |
| Baby RSA (0) (200)                | fwopCTF{13045502302425615144883543017919348302961367754511098998678884785553997741250139993469249405} | `python3 baby_rsa_0` |
| Baby RSA (4) (200)                | fwopCTF{16832067193038570664627710532871887598013604871431045374089410572330773390687} | `python3 baby_rsa_4` |
| Capture the flags (200)           | fwopCTF{eureka8891}               | [International Code of Signals](https://en.wikipedia.org/wiki/International_maritime_signal_flags) |
| Did you take biology? (200)       | fwopCTF{DNARNAGENES}                             | [Codons Genetic Code](https://www.dcode.fr/codons-genetic-code) |
| Hebrew Texts (200)               | fwopCTF{the_water_in_the_black_sea_is_too_salty_aUdhEUjIhO} | [Atbash Cipher](https://gchq.github.io/CyberChef/#recipe=Atbash_Cipher()) |
| talking in the wind (200)         | fwopCTF{COMEFROMTHEWIND}                         | [Navajo Code Cipher](https://www.dcode.fr/navajo-code)             |
| Touch and feel (200)              | fwopCTF{BRAILLE_FUN}                             | [Braille](https://www.dcode.fr/braille-alphabet)                   |
| Elementary, My Dear Watson (300)  | fwopCTF{You_know_my_methods_Watson}              | [Dancing Men Cipher](https://www.dcode.fr/dancing-men-cipher)      |
| This is just ridiculous! (300)    | fwopCTF{so_many_steps}                           | base64 to bytes to base64 to hex to base64 to ascii                |

## 05 Web
|             Challenge             |                      Flag                      |                               Method                               |
| --------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------ |
| In Front Of Your Eyes (100)       | fwopCTF{Wolfy_The_Wolf}                        | [Link](https://web.fweefwop.club/in_front_of_ur_eyes.html) View page source |
| Marq-weeeeeee! (100)              | fwopCTF{t3f0n00}                               | [Link](https://web.fweefwop.club/weee.html) `curl -sSL https://web.fweefwop.club/weee.html | grep fwopCTF{` |
| No Inspector (100)                | fwopCTF{funky_0n_4_fr1day_n1ght}               | [Link](https://web.fweefwop.club/no_inspector.html) View JS script      |
| Robot Invasion (100)    | fwopCTF{k1ller_r0bots_wilL_rUl3_th3_W0rld!!1}  | [Link](https://web.fweefwop.club/robot_invasion.html) `curl https://web.fweefwop.club/robots.txt` `curl https://web.fweefwop.club/totally_evil_plan` |
| Wacky CSS (100)                   | fwopCTF{Take_my_hand_to_your_fantasy}          | [Link](https://web.fweefwop.club/wacky_css.html) View CSS file     |
| Complete me (200)                 | fwopCTF{where}                                 | SQL Select From Where                                              |
| Cookies (250)                     | fwopCTF{Nom_nom_cookies}                       | Inspect element -> Application -> user changed to COOKIE MONSTER   |
| client side login (300)           | fwopCTF{SFOVF5TENW}                            | Type `_bef____a_` into login box or type `document.getElementById("text").innerHTML.substring(1080, 1100)` into browser console |
| 53Cr37 8r0W53r (400)       | fwopCTF{secret_browser_007} | [Link](https://web.fweefwop.club/cookie.php) Inspect -> More tools -> Network conditions -> User agent A3SECRET or `curl https://web.fweefwop.club/agent.php -H 'user-agent: A3SECRET'` |
| KevinSay (400)                    | fwopCTF{C0MM4ND1NDJ3C710N11}                   | [Link](http://web.fweefwop.club:8401/) `$(ls)` `$(cat flag193290.txt)` |
| weird requests huh (400)          | fwopCTF{what_does_put_even_do??} | [Link](https://web.fweefwop.club/requests.php) `curl -X PUT https://web.fweefwop.club/requests.php` |
| SQLI (500)                        | fwopCTF{Leaked_data_123}                       | [Link](http://web.fweefwop.club:8400/login.php) [SQL Injection](https://d00mfist.gitbooks.io/ctf/content/sql-injections.html) username and password: `'--` or `' OR '1'='1` |
| SQLI But Filtered? (600)          | fwopCTF{f1lt3rs_not_good_3n0ugh}               | [Link](http://web.fweefwop.club:8402/login.php) (can't have injection start with `'`) username and password: `-'` |


## 06 Reverse
|             Challenge             |                            Flag                            |                               Method                               |
| --------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------ |
| Reversing Python 1 (100)          | fwopCTF{no_python_required}                                | `cat Reverse1.py`                                                  |
| Reversing Python 2 (150)          | fwopCTF{perhaps_this_is_the_flag}                          | `cat Reverse2.py`                                                  |
| Reversing Python 3 (175)          | fwopCTF{see_seesaw_sheshore_see_sheshore_seasells_shells}  | `cat Reverse3.py`                                                  |
| Reversing Python 3 Bonus (250)    | fwopCTF{a505d061c2baf118fce231d8bfc7c1cbad34ccf7f2ed2c4b8b8c675c235fd744}  | `grep -E 'kaq8h|nw91' Reverse3EXTRA.py`            |
| Reversing Python 4 (250)          | fwopCTF{then_if_then_else_if_if}                           | Paste code into python terminal                                    |
| Reversing Python 5 (275)          | fwopCTF{bonucleicryxriluoxe}                               | Paste code into python terminal                                    |
| Reversing Python 6 (300)          | fwopCTF{also_crypto_lol}                                   | Paste code into python terminal                                    |
| Reversing Python 7 (350)          | its_time_t;qfwopCTF{                                       | String starts at index 12 and ends at ; and is 20 length           |
| Fwop Door (500)                   | fwopCTF{quite_a_long_flag_for_reverse_eng_dont_you_think_so} | `python3 fwop_door.py`                                           |
| Reversing Python 8 (500)          | fwopCTF{arrays_hold_things}                                | Brute force character by character                                 |

## 07 OSINT
|             Challenge             |                Flag                |                               Method                               |
| --------------------------------- | ---------------------------------- | ------------------------------------------------------------------ |
| A street named what? (100)        | fwopCTF{Pruneridge}                | 3896 Pruneridge Ave                                                |
| Where is everybody? (100)         | fwopCTF{Valencia} | https://www.ladbible.com/community/viral-time-traveller-from-2027-visits-mcdonalds-after-human-extinction-20210514 |
| Kevin Gaming (200)                | fwopCTF{ps2}                       | [Twitter](https://twitter.com/TheCoolerKevin_) Follow him on twitter to get birth year |
| Kevin Took The Flag (250)         | fwopCTF{wayback_machine_doesn't_let_me_play_club_penguin_again_D:} | [Twitter](https://twitter.com/TheCoolerKevin_) Wayback Machine |
| Location Location Location (200)  | fwopCTF{Kinshasa}                  | (-4.396,15.317)                                                    |
| Kevin's secret (275)              | fwopCTF{h1dd3n_1n_7h3_h1570ry_28934} | Go to the forked repo, see last commit edit                      |
