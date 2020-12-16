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

def is_prime_brute_force(check_num):
    # flag, start by assuming value is non-prime
    prime = False
    # check two base cases, both are primes
    if check_num == 1:
        return True # 1 is NOT prime, don't bother with it and don't count it
    elif check_num == 2:
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
        return True
    else: return False # haven't found one, report that

# mark the starting time
start_time = time.time()
# check n numbers for primality, start at 3, step by 1
check_up_to = 100000 # amount of numbers to check
for j in range(3, check_up_to, 1):
    # call to is_prime() with j iterator and
    # unpack returns, avoid calling back twice for bool and number found
    prime_found = is_prime_brute_force(j)
    if prime_found:
        num_primes_found += 1
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
# changed the algo to only iterate the number of primes counter
# after the function returns
# doesn't make it any more efficent though, still 63 seconds

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

# now a test that checks if the last digit is 0, 2, 4, 6, or 8

import time

# counter for primes found
num_primes_found = 1 # start at one, 2 is prime

# this code aims to skip even numbers more effeciently
def is_prime_skip_2s(check_num):
    # prime flag, assume false
    prime = False
    # checks for 1 and 2
    # commenting out because I start on 3,
    # shouldn't be required
    #if check_num == 1 or check_num == 2:
    #    return True
    # go into for loop as with brute force
    # this time, start on 3 and step by 2, avoid even numbers
    for i in range (3, check_num, 2):
        # but check first if the last number is divisible by 2
        # I've decided to cast to binary then check last index of
        # byte rather than divide, we'll see how this goes
        # this is bad for execution
        #if bin(check_num)[-1] == 0:
        #    # is even and not 2, can't be prime
        #    prime = False
        #    break
        # check if check_num is divisible by the odds given by
        # i
        # commenting out the binary checks
        if check_num % i == 0:
            # stop once we find a number that divides into
            # check_num
            prime = False
            break
        # number wasn't even and isn't divisible by i, must be prime
        else:
            prime = True
    # now figure out what to return
    if prime == True:
        return True
    else:
        return False

# mark the starting time
start_time = time.time()
# check n numbers for primality, start at 3, step by 1
check_up_to = 100000 # amount of numbers to check
for j in range(3, check_up_to, 2): # changing step to 2
    # check return value from is_prime_skip_2s()
    if is_prime_skip_2s(j):
        num_primes_found += 1
        print(j, "is reported as prime")

# calculate and report benchmark
# truncate and format time
end_time = format(abs(time.time() - start_time), '.2f')
print("Prime test of", check_up_to, "took:", end_time, "seconds")
print("Found:", num_primes_found, "prime numbers")

# this is a very poor algorithm.
# it counts the right number of primes, 9,592, but takes 
# about 216 seconds
# very, very bad algorithm compared to the brute force.
# could be related to casting the int to binary and checking the
# LSB. Might be better just to not feed the function even numbers
# using the for loop that calls the function, starting on 3 and stepping
# by 2, will test now
# commenting out the binary LSB check and stepping by 2 to avoid
# feeding the function even numbers has reduced the benchmark time from
# 213 seconds to 172 seconds
# still not nearly as good as the brute force function
# more investigation required.
# UPDATE:
# changed the code to skip even numbers from being sent into the function
# also changed the function not to check for divisibility by even numbers
# time reduced to 33 seconds. Looks like we've got a winner
# getting an off by one error on the reported number of primes though

#%%
# test code
"""
even_num = 12
odd_num = 13

if bin(even_num)[-1] == 1:
    print('that worked for even', bin(even_num)[-1])
if bin(odd_num)[-1] == 1:
    print("that worked for odd", bin(odd_num)[-1])


print(bin(even_num)[-1])
print(bin(odd_num)[-1])


for i in range(len(bin(even_num))):
    x = int(i)
    print(bin(even_num)[i], sep='', end='')
    #print(bin(odd_num)[i], sep='', end='')
    
print("\n")
for i in range(len(bin(odd_num))):
    x = int(i)
    print(bin(odd_num)[i], sep='', end='')

"""























