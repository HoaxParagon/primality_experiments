# primality experiments in python
The public repo of a B.Sc. CS student's experiments with primality algorithms. This code was made with little mathematical research. I'm not a mathematician nor do I pretend to be. I'm sure there are better ways to calculate prime numbers.

Code tested on a watercooled 8-core AMD 8350 Black using Spyder IDE and Python 3.8 or greater  
The correct number of primes of a test of 100,000 ints is 9,592.  

### Definitions:
* prime number: a number divisible only by itself and 1. except for 2, always odd
* semiprime: a number divisible by itself, 1, and two prime numbers


### Bruteforce test:
tested on ints up to 100,000
about 63 seconds to find 9,592 primes  
Could be better, the algorithm is very slow. Unsure of time complexity, linear perhaps?  
Would likely be faster if I didn't print every prime to console but I'm not printing  
   inside the for loop, only once per prime


### Skipping even numbers test:
again, tested on ints up to 100,000  
checking for evens bytewise was a poor  
idea, ended up in execution times upwards of 210 seconds  
changed it to skip sending even numbers and changed  
the function to not check if the value is divisible by  
even numbers  
This reduced the execution time from 210 to about 33 seconds  


### Explicit prime test:
checks 100,000 numbers for primality  
most efficent algorithm yet  
takes about 12 seconds to find 9,592 primes  
checks the number only on primes up to the number  
also skips checking even numbers using steps in a for loop  


### TODO:
- [ ] implement graphing for these tests  
   time vs number of tested?  

- [ ] export graph photos and either learn about O notation  
   or, speculate until the need to question sanity becomes overwhelming  
- [ ] upload comparative C++ code and times  
- [ ] upload executables created with pyinstaller  
