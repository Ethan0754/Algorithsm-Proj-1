# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:17:05 2024

@author: huynh
"""

import math
import random
        
#---------------------------Front end---------------------#
def options():
    print("Please select your user type\n\t1.) A public user\n\t2.) The owner of the keys\n\t3.) Exit Program")
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
#**************************Key Generation****************#

def is_prime(prime_num):
    
    x = random.randint(2, prime_num)
    y = prime_num-1
    if(pow(x,y,prime_num) != 1):
        return False
    
    
    
    if prime_num < 2:
        return False
    
    for i in range(2, math.floor(math.sqrt(prime_num))):
        if (prime_num%i) == 0:
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


def extended_gcd(a =1, b = 1):
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
    
    d = x%phi
    
    return n, e, d

#**************************Key Generation****************#

#**************************Encryption and Decryption*****#
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
    
        

#---------------------------Main-------------------------#

n, e, d = generateKeys()
print ("Public Keys: ", n, e)
print ("Private Key: ", d)


eList = encryption("Hi")
print (eList)

dList = decryption(eList)
print (dList)


    



     

