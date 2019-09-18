# cipher

This program performs an encryption algorithm on an unencrypted method given in the file 'encrypt.txt'. It then performs the opposite process on an encrypted message given in 'decrypt.txt'. The results from each operation are printed to the console.

The encryption uses a simple algorithm, in which the unencrypted message is placed in a k x k matrix in **row major order**. The smallest possible dimensions are selected for the matrix. So given a string of length, n, the dimension, k, equals the square root of n rounded up to the nearest integer. This results in blank spaces in the matrix that follow the end of the string. 
The matrix is then read in **column major order**, skipping any blank spaces, which creates the encrypted message. (in the code, an asterisks is used to denote a blank space)

The decryption method reads the length of the encrypted string, creates the k x k matrix, and calculates how many cells on the matrix will be blank space. It then fills in the askterisks to denote a blank space, starting from cell (k,k), moving in reverse row-major order. Then the encrypted message is filled in in column-major order, skipping blank space cells. The matrix is then read in regular row-major order, stopping at the first asterisks. This is the decrypted messasge.

The format of 'encrypt.txt' and 'decrypt.txt' is the same. The first line is an integer that represents the number of messages to encode/decode within the text file. Blank lines are skipped. For a given number, n, in the initial (index 0) line, any text after the nth line is ignored. 
