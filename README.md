# primality_experiments
A public repo of a B.Sc. CS students experiments with primality algorithms. This code was made with little mathematical research. I'm not a mathematician nor do I pretend to be. I'm sure there are better ways to calculate prime numbers.

Code tested on a watercooled 8-core AMD 8350 Black using Spyder IDE and Python 3.8 or greater  
The correct number of primes of a test of 100,000 ints is 9592.  

### Definitions:
* prime number: a number divisible only by itself and 1. except for 2, always odd
* semiprime: a number divisible by itself, 1, and two prime numbers


### Bruteforce test:
tested on ints up to 100,000
about 63 seconds to find 9,592 primes  
Could be better, the algorithm is very slow. Unsure of time complexity, linear perhaps?  
Would likely be faster if I didn't print every prime to console but I'm not printing  
   inside the for loop, only when the function returns  
