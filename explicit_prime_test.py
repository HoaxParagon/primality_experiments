# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:49:27 2020

@author: HoaxParagon @ github[dot]com/HoaxParagon
         All rights reserved
         
         
This one seeks to explicitly check each argument for primatlity
by checking for division by first five primes
and by a list of primes already found by the function itself

"""
import time

# prime_list is a place to store values found to be checked against
prime_list = [2, 3, 5, 7, 11] # an ordered list of primes
num_primes_found = 5 # start at 5, list contains first five
is_prime = False # flag, assumes false

def explicit_prime_test(check_num):
    # continue checking for the length of prime list
    # and the four conditionals
    num_yet_to_check = int(len(prime_list))
    # check for cases of the first four primes
    # commenting this out,
    # avoid these checks everytime and 
    # just start at 11 for optimization
    #if check_num == 2       \
    #    or check_num == 3   \
    #    or check_num == 5   \
    #    or check_num == 7   \
    #    or check_num == 11:
    #    return True
    while num_yet_to_check:
         #division by 2, covers division by even numbers
        # these checks are redundant,
        # comment out for optimizing
        # if check_num % 2 == 0:
        #     is_prime = False
        #     break
        # elif check_num % 3 == 0:
        #     is_prime = False
        #     break
        # elif check_num % 5 == 0:
        #     is_prime = False
        #     break
        # elif check_num % 7 == 0:
        #     is_prime = False
        #     break
        # elif check_num % 11 == 0:
        #     is_prime = False
        #     break
        # else:
        
        for i in range(0, int(len(prime_list)), 1):
            #print("checking against:", prime_list[i])
            if check_num % prime_list[i] == 0:
                is_prime = False
                # won't need to check any others, found even divisibilty
                num_yet_to_check = 0
                break
            else: # went through all previous conditionals and checked
                # the list up to now, update flag, might have found it
                is_prime = True
        # completed test of
        # values in list, break from while
        break
    # now return bool, report primality
    if is_prime:
        prime_list.append(check_num)
        return True
    else: return False

# mark the starting time
start_time = time.time()
# check n numbers for primality, start at 3, step by 1
check_up_to = 100000 # amount of numbers to check
# start at 3, check only odds
for j in range(11, check_up_to, 2):
    # call to explicit_prime_test() with j iterator and
    # unpack returns, avoid calling back twice for bool and number found
    prime_found = explicit_prime_test(j)
    if prime_found:
        num_primes_found += 1
        print(format(j, ','), "is reported as prime")

# calculate and report benchmark
# truncate and format time
end_time = format(abs(time.time() - start_time), '.2f')
print("Prime test of", format(check_up_to, ','), "took:", end_time, "seconds")
print("Found:", format(num_primes_found, ','), "prime numbers")

'''
this is my fastest algorithm yet
takes about 11 seconds to find the 9,592 primes between 0 and 100,000
and about 570 seconds to find the 78,498 primes between 0 and 1,000,000

I only tested 1 million for fun, all other scripts use 100,000 to 
benchmark

this time I created a list to check against to avoid needless division.
From what I understand, this is called memoization.
the list is seeded with the first 5 prime numbers, 2, 3, 5, 7 and 11
then the function takes an iterator argument, j, and checks it against 
the values contained in the list up to the number j.
'''

















