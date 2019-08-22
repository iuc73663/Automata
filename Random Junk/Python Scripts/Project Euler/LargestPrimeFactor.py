# -*- coding: utf-8 -*-
"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
count = 0
n= 600851475141

def isPrime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True


while count == 0:
    print(n)
    if 600851475143%n == 0:
        print(n)
        if isPrime(n) == True:
            print(n)
            count = 1
    else:
        n = n - 2
        
    if n%100 == 0:
        print(n)