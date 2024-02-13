# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:17:05 2024

@author: Thi Huynh, Ethan Pendergraft, Hunter Henderson
"""

import math
import random
        
#---------------------------Front end---------------------#
def options():
    print("Please select your user type")
    print("\t1.) A public user")
    print("\t2.) The owner of the keys")
    print("\t3.) Exit Program")
    userInput = input("Enter your choice: ")
    return userInput

def pubUser():
    print("As a Public User, what would you like to do?")
    print("\t1.) Send an encrypted message")
    print("\t2.) Authenticate a digital signature")
    print("\t3.) Exit\n")
    option = input("Enter your choice: ")
    return option

def owner():
    print("As the owner of the keys, what would you like to do?")
    print("\t1.) Decrypt a received message")
    print("\t2.) Digitally sign a message")
    print("\t3.) Show the keys")
    print("\t4.) Generating a new set of keys")
    print("\t5.) Exit")
    option = input("Enter your choice: ")
    return option
    
#---------------------Back end----------------------------#

#**************************Key Generation****************************#

def is_prime(prime_num):
    
    if prime_num < 2:
        return False
    
    x = random.randint(2, prime_num)
    y = prime_num-1
    
    if(pow(x,y,prime_num) != 1):
        return False
    
    for i in range(2, math.floor(math.sqrt(prime_num))):
        if (prime_num % i) == 0:
            return False
    return True
    
def genPrime(minimum, maximum):
    
    prime = random.randint(minimum, maximum)

    while (is_prime(prime) == False):
        prime = random.randint(minimum, maximum)
    return prime
    
    
def gen_relative_prime(phi):
    
    e = random.randint(2, phi)
    while math.gcd(e, phi) != 1:
            e = random.randint(2, phi)
    return e


def extended_gcd(a = 1, b = 1):
    "Chapt1_Number_and_encryption Page 23"
    if b == 0:
        return (1, 0, a)
    (x, y, z) = extended_gcd(b, a%b)
    return y, x - a//b*y, z
    

def generateKeys():
    min_prime = 50
    max_prime = 500

    p = genPrime(min_prime, max_prime)
    q = genPrime(min_prime, max_prime)

    while (p == q):
        q = genPrime(min_prime, max_prime)
        
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = gen_relative_prime(phi)
    x, y, z = extended_gcd(e, phi);
    
    d = x % phi
    
    return n, e, d


#**************************Encryption and Decryption**********************#

def encryption(m):
    full = []
    x = list(m)
    for num in m:
        x = ord(num)
        y = pow(x, e, n)
        full.append(y)
    return full

def decryption(eList):
    m = ""
    for num in eList:
        y = pow(num, d, n)
        x = chr(y)
        m += x;
    return m
    
#**************************Signatures************************************#
        
def authSig(s, m):
    mList = ''
    for num in s:
        y = pow(num,e,n)
        x = chr(y)
        mList += x;
    if(mList == m):
        print("Signature is valid\n")
    elif (mList != m):
        print("Signature is NOT valid\n")
        
    
def genSig(m):
    s = []
    x = list(m)
    for num in m:
        x = ord(num)
        y = pow(x, d, n)
        s.append(y)
    return s
    
    
#---------------------------Main-------------------------#

# Generate Keys: public key = (n, e), private key = d
n, e, d = generateKeys()
puKey = [n , e]
pvKey = d
print ("RSA keys have been generated")

messages = []           # Stores Encrypted messages
sigs = []               # Stores signatures
sig_user_input = []     # Needed to store user-input for authentification because authSig requires two parameters
opInput = options()     # Opens 'options' menu

# User Interface
while opInput != '3':

    if opInput == '1':                                          
           pub = pubUser()                                      # Send Encrypted Message
           if pub == '1':
               userMessage = input("Enter message: ")
               eList = encryption(userMessage)
               messages.append(eList)
               print ("Message has been encrypted\n")
           elif pub == '2':                                     # Authenticate Signature
               if len(sigs) == 0:
                   print ("\nThere are no signatures to authenticate\n")
               else:
                   print ("The following messages are available")
                   for i in range (0, len(sigs)):               # Print options
                          print(i + 1, ".", sig_user_input[i])
                   sigOptions = int(input("\nEnter your choice: "))
                   sigOptions -= 1                                  # Subtract 1 because user input sees i + 1
                   while sigOptions not in range (len(sigs)):
                       print("\nIncorrect Value entered\n")  
                       sigOptions = int(input("\nEnter your choice: "))
                       sigOptions -= 1
                   a_Sig = authSig(sigs[sigOptions], sig_user_input[sigOptions])  # Calls function to authenticate
           elif pub == '3':
               opInput = options()
           else:
               print("\nIncorrect Value Entered\n")
    elif opInput == '2':                                        # Decrypt message
            own = owner()
            if own == '1':
                if len(messages) == 0:
                    print("There are no messages to decrypt!")
                else:
                    print ("The following messages are available")
                    for i in range (0, len(messages)):          # Print options
                           print(i + 1, '. (length = ', len(messages[i]), ')')       
                    strOption = int(input("\nEnter your choice: "))
                    strOption -= 1
                    while strOption not in range (len(messages)):
                        print("\nIncorrect Value entered\n")  
                        strOption = int(input("\nEnter your choice: "))
                        strOption -= 1
                    dList = decryption(messages[strOption])
                    print ("Decrypted Message: ", dList, '\n')
            elif own == '2':                                    # Digitally sign a message
                mySig = input('Enter a message: ')
                signature = genSig(mySig)
                sigs.append(signature)                          # Store generated signature in a list
                sig_user_input.append(mySig)                    # Store user-input-message in a list
                print("Message signed and sent\n")
            elif own == '3':                                    # Show current public & private keys
                print('Public Key: ', puKey)
                print('Private Key: ', pvKey)
            elif own == '4':                                    # Generate new set of Keys
                n, e, d = generateKeys()
                puKey = [n , e]
                pvKey = d
                print ("\nNew Keys Generated!\n")
            elif own == '5':
                opInput = options()
            else:
                print("\nIncorrect Value Entered\n")
    elif opInput == '3':
            break
    else:
            print("\nIncorrect Value Entered\n")                # Re-prompt for options value          
            opInput = options()
            
print ("Bye for now!")



""""
#-----------------Testing------------------#


n, e, d = generateKeys()
pvKey = [n , e]
puKey = d
print ("Public Keys: ", pvKey)
print ("Private Key: ", puKey)


userMessage = input("Enter Sentence to encrypt: ")

eList = encryption(userMessage)
print ("Encrypted Message: ", eList)

dList = decryption(eList)
print ("Decrypted Message: ", dList)


userInput = input("Enter a signature: ");
s = genSig(userInput)

authSig(s, userInput)

"""