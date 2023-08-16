## Hello World Primer

### Creating a C Program in Replit
Prerequistes: have a Replit account

1. Log into Replit
1. Click **Create Repl**
1. Search for and select C template
1. Name your program **My First Program**

![tempsnip](https://github.com/it-academy-svhec/intro-to-programming/assets/61634762/6275c3cf-4b9f-4d83-ba3f-f43387a9499b)

**Source code files are on the left and the CLI (command-line interface) is on the right.**

### Writing Your First C Program
1. Clear the source code from the file
1. Enter the following source code line by line.

    ```C
    #include <stdio.h>
    
    int main(void) {
      printf("Hello World\n");
      return 0;
    }
    ```

1. You can invoke the GNU C Compiler by using the `gcc` command in the Replit CLI. This command takes a variety of parameters, which can be shown by running `gcc --help`. Remember, source code has to be compiled to machine code before it can execute on a computer. The compiler generates binary instructions for the computer based on source code written in languages like C and C++.

    Compile your main.c file into a binary executable program by running the following command:

        gcc main.c

1. Now, run `ls` to print the contents of the working directory and show the compiled program. You should see a file named `a.out`, which is the program compiled from the `main.c` source code file.

1. In order to run an executable file or script on Linux/UNIX systems, you must prefix the name of the file with `./`. This assumes you are in the same directory as the file. Run the following command to run your program. By default, on Linux/UNIX systems, the `.out` file extension is used to denote executable files compiled from C source code.

        ./a.out

1. You should see the following output on the terminal:

        Hello World

### Naming Programs
1. Let's compile the program again program but this time give it a friendly name such as `hello_world`. The `-o` parameter allows you to name the compiled binary executable file. Run the following command to create a program called `hello_world`:

        gcc -o hello_world main.c

1. Run `ls` to confirm that the program is showing.

1. The old `a.out` program should still be there, but you can delete that with the following command:

        rm a.out
