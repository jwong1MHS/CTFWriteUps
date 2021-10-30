Link: https://ctf.fweefwop.club/challenges

## 01 General
|             Challenge             |              Flag              |                             Method                             |
| --------------------------------- | ------------------------------ | -------------------------------------------------------------- |
| Assembly Warm Up (100)            | fwopCTF{Assembly}              | Google/Common Knowledge                                        |
| Base2 (100)                       | fwopCTF{11101000}              | [Hex to Decimal](https://www.rapidtables.com/convert/number/hex-to-decimal.html) |
| Base64 Abridged (100)             | fwopCTF{SSBsb3ZlIENURg==}      | ASCII to Base64 [CyberChef](https://gchq.github.io/CyberChef/#recipe=To_Base64('A-Za-z0-9%2B/%3D')) |
| Hex the way in (100)              | fwopCTF{back_from_hex}         | Hex to ASCII [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')) |
| Jon Us in Discord (100)           | fwopCTF{fweefwop_ctf_go_go_go} | [Discord Link](https://discord.gg/y2BXfQCgmN)                  |
| Name this language (6) (100)      | fwopCTF{BASIC}                 | Google                                                         |
| Touch the base (100)              | fwopCTF{base64_is_everywhere}  | Base64 to ASCII [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)) |
| Warm Up -- Let's Start! (100)     | fwopCTF{this_is_the_flag}      | Copy/paste                                                     |
| Zeros and Ones (100)              | fwopCTF{complicated}           | Binary to ASCII [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)) |
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
| What is that thing? (3) (150)     | fwopCTF{icmp}                  | [Common Protocols](https://en.wikibooks.org/wiki/Network_Plus_Certification/Technologies/Common_Protocols) |
| What's that thing? (0) (150)      | fwopCTF{compiler}              | Common Knowledge                                               |
| What's that thing? (1) (150)      |                                |                                                                |
| What's that thing? (2) (150)      | fwopCTF{switch}                | [Types of Network Devices](https://www.educba.com/types-of-network-devices/) |
| Modular (0) (200)                 | fwopCTF{4}                     | Wolframalpha/Mental math                                       |
| Modular (1) (200)                 | fwopCTF{31}                    | [WolframAlpha](https://www.wolframalpha.com/input/?i=x+*+11+%3D+46+%28mod+59%29) |
| Modular (2) (200)                 | fwopCTF{194}                   | [WolframAlpha](https://www.wolframalpha.com/input/?i=x*x+%3D+2+%28mod+607%29) |
| NASM (2) (200)                    | fwopCTF{9}                     | Line 13 of hello.asm                                           |
| XOR warm up (200)                 | fwopCTF{xor_rules}             | XOR with key 01 [CyberChef](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Hex','string':'01'%7D,'Standard',false)) |
| NASM (1) (250)                    | fwopCTF{i_have_done_this_ex}   | [Online NASM Emulator](https://rextester.com/l/nasm_online_compiler)  |
| Go through some gates (300)       | fwopCTF{1}                     | [Digital Logic](https://www.circuitbasics.com/what-is-digital-logic/) |
| Assembly: Jump (400)              | fwopCTF{fwop}                  | Line 33 from 0x0? to 0x0d                                      |
| Modular (4) (400)                 | fwopCTF{278505}                | `pow(31, pow(31, 2813771283, totient(384302), 384302)`         |

## 02 Forensics
|             Challenge             |                Flag                |                               Method                               |
| --------------------------------- | ---------------------------------- | ------------------------------------------------------------------ |
| Alice in Wonderland? (100)        | fwopCTF{Beneath_the_surface}       | `strings garden.jpg`                                               |
| Just inflate me (100)             | fwopCTF{ok_you_found_me}           | `gunzip flag.txt.gz`                                               |
| Not Viewable (100)                | fwopCTF{actually_an_image}         | change `fflag.txt` to `fflag.png` or `fflag.jpg`                   |
| The Meta Joke (100)               | fwopCTF{metadata_is_funky}         | `file MyCoolCard.jpg`                                              |
| Not the same (150)                | fwopCTF{r3sp3ct_th3_d1ff}          | `diff t1.txt t2.txt`                                               |
| Reading between the Eyes (150)    | fwopCTF{r34d1ng_b37w33n_7h3_by73s} | [Steganography Online](https://stylesuxx.github.io/steganography/) |
| Sharper Image (150)               | fwopCTF{this_is_a_boring_flag}     | `base64 -d bb.txt  > bb.png`                                       |
| Bitcoin Laundering (0) (200)      | fwopCTF{20000}                     | `cat transactions.json | grep -o -i { | wc -l`                     |

## 03 Linux Lab
|             Challenge             |                Flag                |                               Method                               |
| --------------------------------- | ---------------------------------- | ------------------------------------------------------------------ |
| Linux Lab Level 1 (100)           | fwopCTF{level_1_u3xe4}             | `ssh level0@linux.fweefwop.club`, Password: fwopCTF{level_0}, `ls` |
| Linux Lab Level 2 (100)           | fwopCTF{level_2_l46h3}             | `cd subdir`, `ls`                                                  |
| Linux Lab Level 3 (100)           | fwopCTF{level_3_ti8fx}             | `cat flag.txt`                                                     |
| Linux Lab Level 4 (100)           | fwopCTF{level_4_nmc4e}             | `env`                                                              |
| Linux Lab Level 5 (100)           | fwopCTF{level_5_4gw}               | A lot of `ls` and `cd` and autocomplete with <kbd>Tab</kbd>        |
| Linux Lab Level 6 (100)           | fwopCTF{level_6_3bw}               | `cat flag.txt | grep -i fwopCTF{`                                  |
| Linux Lab Level 7 (100)           | fwopCTF{level_7_82j}               | `cat .flag.txt`                                                    |
| Linux Lab Level 8 (100)           | fwopCTF{level_8_2b3}               | `cat flag.png`                                                     |
| Linux Lab Level 9 (100)           | fwopCTF{level_9_c2p}               | `diff f1.txt f2.txt`                                               |
| Linux Lab Level 10 (100)          | fwopCTF{level_10_fqd}              | `cat ./-cant_touch_this`                                           |
