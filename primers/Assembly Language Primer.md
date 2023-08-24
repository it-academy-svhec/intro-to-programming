# Assembly Language Primer

Pep9 is a virtual assembly language created by Pepperdine University to teach their computer science students. You practice writing some basic assembly programs.

## Pep9 Assembler Installation and Basic Usage
1. Download the Pep9 assembler from this link: [download link](https://computersystemsbook.com/5th-edition/pep9/).

1. Install the program

1. Review the Pep9 interface

![pep9 interface](https://github.com/it-academy-svhec/intro-to-programming/assets/61634762/cdf8a07d-28da-4838-9f91-c1b344a86788)


## Hello World Program
1. Open the Pep/9 program

1. Enter the following source code into the **Source Code** section of the editor
 
```
;A program to output "Hi"
;
LDBA    0x000D,d    ;Load byte accumulator 'H'
STBA    0xFC16,d    ;Store byte accumulator output device
LDBA    0x000E,d    ;Load byte accumulator 'i'
STBA    0xFC16,d    ;Store byte accumulator output device
STOP                ;Stop
.ASCII  "Hi"        ;ASCII "Hi" characters
.END
```
**Source: Stan Warford**
