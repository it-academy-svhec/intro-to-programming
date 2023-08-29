# Assembly Language Primer

Pep9 is a virtual assembly language created by Pepperdine University to teach their computer science students. You practice writing some basic assembly programs.

## Pep9 Assembler Installation and Basic Usage
1. Download the Pep9 assembler from this link: [download](https://computersystemsbook.com/5th-edition/pep9/).

1. Install the program

1. Review the Pep9 interface

The **Accumulator** stores data that the CPU can process later. We can load data to and from the **Accumulator**.

![pep9 interface](https://github.com/it-academy-svhec/intro-to-programming/assets/61634762/cdf8a07d-28da-4838-9f91-c1b344a86788)

## Basic Addition
Let's write a program that adds two numbers and prints the result. Comments are prefixed with a semicolon `;`. Keep in mind that this is very similar to how your computer would add numbers when you use a calculator application. The CPU is very powerful but requires specific instructions to do anything. Without binary instructions, the CPU is just a dumb silicon chip, a paperweight.

1. Open the Pep/9 program

1. Enter the following source code into the **Source Code** section of the editor:

   ```
   LDWA 0x0031,i    ;Load the decimal number 1 into the accumulator
   ADDA 0x0001,i    ;Add 1 to the accumulator
   STBA 0xFC16,d    ;Store value in accumulator to the output device
   STOP             ;Stop
   .END
   ```
   Note that the number 1 in ASCII is 0x0031 in hexadecimal. First, we load 1 into the accumulator using its ASCII representation. Then we add 1 to the accumulator. Next we store the value of the accumulator into the output device. Finally, program executation stops.

1. Save the program and call it **Basic Addition**

1. Click the green play button to run the code

1. Note how the **Output** box is filled in and the **Assembler Listing** shows the hexadecimal object code, the mnemonic (instruction name), and memory address location in hexadecimal.

 ![image](https://github.com/it-academy-svhec/intro-to-programming/assets/61634762/438affa3-86f8-46a2-8843-0c07125f50e2)
 **Adding two numbers and printing the result in Pep9**

## Add One to a Different Number
Let's modify the previous program to initialize the accumulator to `5` this time. Then we will add 1 to it like last time.

Use the following ASCII chart to reference the hex value required: [ASCII Table](https://www.rapidtables.com/code/text/ascii-table.html)

1. Change the line `LDWA 0x0031` to add the ASCII hexadecimal representation of `5`

1. Save the program again

1. Run the program and confirm that the output is `6`

## Basic Subtration
Now you will write a program to subtract two numbers and display the result.

1. Click **File** > **New**

1. Enter the following code into the **Source Code** section:

   ```
   LDWA 0x0037,i    ;Load the decimal number 7 into the accumulator
   SUBA 0x0001,i    ;Subtract 1 from the accumulator
   STBA 0xFC16,d    ;Store value in accumulator to the output device
   STOP             ;Stop
   .END
   ```

1. Save the program and name it **Basic Subtraction**
