#Efficient Prime Factorization

import math
primes = []
factors = []

#prime list 
def primeList():
  for num in range(2,100):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       primes.append(num)
  return primes
    
#Sort by common factors
def Factors():
  n = 24
  for i in range(len(primes)):
    while n % primes[i] == 0: 
        n = n / primes[i]
        factors.append(primes[i]) 
  print(factors) 
    
primeList()
Factors()
