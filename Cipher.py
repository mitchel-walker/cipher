#!/usr/bin/env python

#  Description: This program reads two text files, 'encrypt.txt' and 'decrypt.txt' and encrypts  and decrypts
#               the given messages, and prints the respective results. The encryption algorithm involves putting
#               the message in the smallest possible k x k matrix by row, rotating it 90 degrees clockwise, and
#               printing each row, skipping the empty spaces in the mtrix

#  Date Last Modified: 2/7/2019
import math


def encrypt(string):
    #this function encrypts a given string and outputs the encrypted message
    
    #m is lowest square number higher than the message length
    k = math.ceil(len(string)**0.5)
    m = k**2
    #create the array
    arr = []
    #fill the array with the message - line by line
    for i in range(0,m,k):
        line = list(string[i:i+k])
        #if a line has blank spaces at the end of it, fill in an asterisks to denote blank space
        while len(line)<k:
            line.append('*')
        arr.append(line)
    #creates encoded string to return
    code = ''
    arr = list(zip(*arr[::-1]))
    for i in range(k):
        for j in range(k):
            if arr[i][j] != '*':
                code += arr[i][j]
    return code

    



def decrypt(string):
    #this function decrypts a given string

    #m is lowest square number higher than the message length
    k = math.ceil(len(string)**0.5)
    m = k**2
    #initialize k x k array of zeros and fill in the asterisks
    empty = '#'*len(string)
    if len(empty) != m:
        empty += '*'*(m-len(string))
    arr = []
    for i in range(0,m,k):
        arr.append(list(empty[i:i+k]))
    arr = list(zip(*arr[::-1]))
    
    #zip outputs list of tuples, so convert to list of lists
    for tup in range(len(arr)):
        arr[tup] = list(arr[tup])
    #fill in array with code string, skipping asterisks
    it = 0
    for i in range(k):
        for j in range(k):
            if arr[i][j] != '*':
                arr[i][j] = string[it]
                it += 1

    #flip array and return decoded message
    arr = list(zip(*arr))[::-1]
    message = ''
    for i in range(k):
        for j in range(k):
            if arr[i][j] != '*':
                message += arr[i][j]
        
    return message
    



def main():
    #this function performs the necessary encryptions & decryptions and prints respectively
    
    
    #encryption first
    messages = open('encrypt.txt', 'r').readlines()
    #take care of endline characters and empty lines
    for i in range(len(messages)):
        messages[i] = messages[i].strip()
    while '' in messages:
        messages.remove('')
    n = eval(messages[0])
    
    #encrypt each line and print the code
    print("Encryption:")
    for i in range(1,n+1):
        print(encrypt(messages[i]))


    #decryption next
    codes = open('decrypt.txt').readlines()
    #take care of endline characters and empty lines
    for i in range(len(codes)):
        codes[i] = codes[i].strip()
    while '' in codes:
        codes.remove('')
    n = eval(codes[0])
    
    #decrypt each line and print the message 
    print('\nDecryption:')
    for i in range(1,n+1):
        print(decrypt(codes[i]))

main()
