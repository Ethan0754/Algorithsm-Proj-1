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

def is_prime(prime_num):
    
    if prime_num < 2:
        return False
    
    for i in range(2, prime_num):
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

def mInverse(e, phi):
    
    for d in range (3, phi-1):
        if (d * e) % phi == 1:
            return d
    return ("not found")
    

def generateKeys():
    min_prime = 2
    max_prime = 25

    p = genPrime(min_prime, max_prime)
    q = genPrime(min_prime, max_prime)

    while (p == q):
        q = genPrime(min_prime, max_prime)
        
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = gen_relative_prime(phi)
    d = mInverse (e, phi)
    
    return n, e, d


#---------------------------Main-------------------------#

n, e, d = generateKeys()[0], generateKeys()[1], generateKeys()[2]

print ("Public Keys: ", n, e)
print ("Private Key: ", d)



    



     

