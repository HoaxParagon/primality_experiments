

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:32:20 2020

@author: HoaxParagon @ github[dot]com/HoaxParagon
         All rights reserved


experiments in primality testing
skipping even numbers after 2

"""



# now a test that checks if the last digit is 0, 2, 4, 6, or 8

import time
from functools import lru_cache

# counter for primes found
num_primes_found = 1 # start at one, 2 is prime

# this code aims to skip even numbers more effeciently
@lru_cache(maxsize=None)
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
#start_time = time.time()
start_time = time.perf_counter()
# check n numbers for primality, start at 3, step by 1
check_up_to = 100000 # amount of numbers to check
for j in range(3, check_up_to, 2): # changing step to 2
    # check return value from is_prime_skip_2s()
    if is_prime_skip_2s(j):
        num_primes_found += 1
        print(j, "is reported as prime")

# calculate and report benchmark
# truncate and format time
end_time = format(abs(time.perf_counter() - start_time), '.2f')
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
