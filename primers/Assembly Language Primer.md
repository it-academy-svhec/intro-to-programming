# Assembly Language Primer

Pep9 is a virtual assembly language created by Pepperdine University to teach their computer science students. You practice writing some basic assembly programs.

## Pep9 Assembler Installation and Basic Usage
1. Download the Pep9 assembler from this link: [download](https://computersystemsbook.com/5th-edition/pep9/).

1. Install the program

1. Review the Pep9 interface

The **Accumulator** stores data that the CPU can process later. We can load data to and from the **Accumulator**.

![pep9 interface](https://github.com/it-academy-svhec/intro-to-programming/assets/61634762/cdf8a07d-28da-4838-9f91-c1b344a86788)

## Adding Two Numbers
Let's write a program that adds two numbers and prints the result. Comments are prefixed with a semicolon `;`.

1. Open the Pep/9 program

1. Enter the following source code into the **Source Code** section of the editor

   ```
   LDWA 0x0031,i    ;Load the decimal number 1 into the accumulator
   ADDA 0x0001,i    ;Add 1 to the accumulator
   STBA 0xFC16,d    ;Store value in accumulator to the output device
   STOP             ;Stop
   .END
   ```

1. Click the green play button to run the code
 ![image](https://github.com/it-academy-svhec/intro-to-programming/assets/61634762/438affa3-86f8-46a2-8843-0c07125f50e2)
 **Adding two numbers and printing the result in Pep9**

1. Save the program and call it **Hello World**

1. Click the green play button to run the code

1. Note how the **Output** box is filled in and the **Assembler Listing** shows the hexadecimal object code, the mnemonic (instruction name), and memory address location in hexadecimal.

![image](https://github.com/it-academy-svhec/intro-to-programming/assets/61634762/c923e5cb-bdc7-479a-9f29-f00831724abc)

## Simple Modification
Let's modify the program to print the letters `IT`.

1. Change the text `Hi` to `IT`

1. Run the program and check the output

## Modify to Print Longer String
Now, you will create an assembly program to print your first name.

1. Create a new file, save it, and call it **Print first name**

1. Paste the contents from the previous Hello World program

1. Replace the text that is currently being printed with your first name

1. Notice that only the first two letters of your first name print and other strange characters print at the end. This is due to how memory addresses are accessed by the program.
