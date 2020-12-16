# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:32:20 2020

@author: HoaxParagon @ github[dot]com/HoaxParagon
         All rights reserved


experiments in primality testing

"""


# brute force test, check each number
# for divisibilty up to (itself - 1)
# don't check 1, 2 or the checked number against itself

import time
num_primes_found = 1 # start at 1, 2 is prime and this doesn't check
# check it here

def is_prime(check_num, num_found):
    # flag, start by assuming value is non-prime
    prime = False
    # check two base cases, both are primes
    if check_num == 1:
        return True # 1 is NOT prime, don't bother with it and don't count it
    if check_num == 2:
        return True # 2 is prime, don't bother with it
    # begin for loop, brute force primality test
    # checks each number iterativly against 2 though 1 less than
    # the number to check
    for i in range (2, check_num, 1): # start at 2, all numbers are 
        # divisible by 1 and themselves
        if check_num % i == 0: # if 0 is the result, the number is
            # print("Checking: ", check_num, "/", i)
            prime = False
            break # found a number that it's divisible by 2
                  # break from loop
        # might be prime, update flag
        else:
            prime = True
    # after the for, check flag
    if prime == True:
        num_found += 1 # found another, keep count
        return True, num_found
    else: return False, num_found # haven't found one, report that

# mark the starting time
start_time = time.time()
# check n numbers for primality, start at 3, step by 1
check_up_to = 100000 # amount of numbers to check
for j in range(3,check_up_to,1):
    # call to is_prime() with j iterator and
    # unpack returns, avoid calling back twice for bool and number found
    prime_found, num_primes_found = is_prime(j, num_primes_found)
    if prime_found:
        print(j, "is reported as prime")

# calculate and report benchmark
# truncate and format time
end_time = format(abs(time.time() - start_time), '.2f')
print("Prime test of", check_up_to, "took:", end_time, "seconds")
print("Found:", num_primes_found, "prime numbers")

# takes around 83 seconds to find 9592 prime numbers
# UPDATE:
# I did something and reduced this to 65 seconds
# not sure what exactly but I think it was modification
# of the print statement in the function call to is_prime()
# current best: 65 seconds to find 9592 primes in first 100,000
# numbers

'''
Might be faster if:

check last number for divisibility by 2, requires division operation
might not be as fast as checking last number as follows:
if last number is 0, 2, 4, 6, 8
    Don't bother, isn't prime, report false

if last number of number % 2 != 0
    not prime, report false
104, not prime
106, not prime

memoization - hold a table of previously found primes
 and a table of semiprimes

semiprime is a product of two primes

'''

# end block, brute force test
#%%








































