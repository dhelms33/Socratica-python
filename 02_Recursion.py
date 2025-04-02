#Fibonacci, Recursion, and memoization
#completed

#first few terms
#1,1, 2, 3, 5, 13, 21 sum of current term and one before it

import math

class UnusualFunctions:
    """ A class dealing with all the odd functions out there"""
    
    def fibonacci(n):
        """Write a function that returns the fibonacci sequence for the nth term"""
        if n==1:
            return 1
        elif n == 2:
            return 2
        elif n > 2:
            return fibonacci(n-1) + fibonacci(n-2)
class FibonacciTest(UnusualFunctions):
    def fibonacciloop(n):
        for n in range(1,11): #rangedoes not include final num
            return(n, ":", fibonacci(n)) #slows down drastically beyond 35 if test large values

#memoization is the cure
class Memoization:
    fibonacci_cache = {}
    
    def fibonacci_ver2(n):
        #if we have cached the value, then return it
        if n in fibonacci_cache:
            return fibonacci_cache[n]
        
        #compute nth term
        if n==1:
            return 1
        elif n ==2:
            return 2:
        elif n > 2:
            value = fibonacci_ver2(n-1) + fibonacci_ver2(n-2)
            
        #cache the value and return it
        fibonacci_cache[n] = value
        return value
for n in range(1,1001):
    print(n, ":", Memoization.fibonacci(n))
    
from functools import lru_cache
@Lru_cache(maxsize = 1000)
class ReturnV1:
    """cleaner implementation of previous func"""
    def fibonacci(n):
        #Check that the input is a positive int
        if type(n) != int:
            raise TypeError("n must be a positive int")
        if n < 1:
            raise ValueError("n must be a positive int")
        if n ==1:
            return 1
        elif n == 2:
            return 2
        elif n >2:
            return fibonacci(n-1) + fibonacci(n-2)
for n in range(1,501):
    print(n, ":", ReturnV1.fibonacci(n))
#come up with edge cases for 2.1 and -1 or string, it breaks
#lets see how quickly the numbers grow
#compute ratio between consecutive terms
for n in range(1,51):
    print(ReturnV1.fibonacci(n+1)/ReturnV1.fibonacci(n))
#ratios converge to golden ratio
