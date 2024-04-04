## Exercises

Read the following [article](https://ryanstutorials.net/linuxtutorial/piping.php) and answer the questions below. Some questions will require additional research.

1. Write the message "hello everyone" in a file called "test" by redirecting the output of the echo command.
    > Your command : `echo hello everyone > test`
1. Write the message "goodbye" in the same file "test" by redirecting the output of the echo command and without overwriting the content of "test" and check with the cat command
    > Your command : `echo goodbye >> test`
1. Make the ``ls -la`` command redirect to the ``foo`` file
    > Your command : `ls -la > foo`
1. Execute ``find /etc -name *conf*`` command  and redirect errors (only errors) to a file named err.txt 
    > Your command : `find /etc -name '*conf*' > /dev/null 2> err.txt`
1. Repeat the previous exercise, this time redirecting the errors to the linux nothingness.
    > Your command : `find /etc -name '*conf*' 2> /dev/null`
1. Now redirect the standard output and the error output of the ``find /etc -name *conf*`` command to two different files (std.out and std.err)
    > Your command :
1. What does the mkfifo command do?
    > No answer required
1. Create a pipe named "MyNammedPipe". Then execute the pwd command which will transmit the data in this pipe. Then use the cat command to read the contents of your "MyNammedPipe" pipe.
    > Your commands :
1. With cat command, add number the lines in the file /etc/passwd with the command ``nl``
    > Your commands : `sudo cat | nl /etc/passwd`
1. Using the previous nl command, the head and tail commands, display the lines of /etc/passwd between line 7 and line 12
    > Your commands : `cat | nl /etc/passwd | head -12 | tail -6`
