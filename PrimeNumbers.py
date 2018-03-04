# Prime Numbers

primes = []
import math
for num in range(2,102):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       primes.append(num)

print(primes)
