import math

def prime_or_not(num):
    i = 2
    n = round(math.sqrt(num) + 1)
    while i < n:
        if num % i == 0:
            return False
        i += 1
    return True

prime_set = set()
primes = list()
with open('primes.txt','r') as f:
    for l in f:
        primes.append(int(l.rstrip()))
        prime_set.add(int(l.rstrip()))
print('preprocessing done')

for i in range(0,2000):
    # print(i)
    for j in range(0,i+1):
        
        num = int(str(primes[i])+str(primes[j]))
        if num > primes[-1]: flag = prime_or_not(num) 
        else: flag = num in prime_set 
        if not flag: continue 

        num = int(str(primes[j])+str(primes[i]))
        if num > primes[-1]: flag = prime_or_not(num) # True if num is prime
        else: flag = num in prime_set 
        if not flag: continue # if num is not prime, then move on to the next set

        for k in range(0,j+1):
            
            num = int(str(primes[i])+str(primes[k]))
            if num > primes[-1]: flag = prime_or_not(num) 
            else: flag = num in prime_set 
            if not flag: continue 
        
            num = int(str(primes[j])+str(primes[k]))
            if num > primes[-1]: flag = prime_or_not(num) # True if num is prime
            else: flag = num in prime_set 
            if not flag: continue # if num is not prime, then move on to the next set
    
            num = int(str(primes[k])+str(primes[i]))
            if num > primes[-1]: flag = prime_or_not(num) 
            else: flag = num in prime_set 
            if not flag: continue 
        
            num = int(str(primes[k])+str(primes[j]))
            if num > primes[-1]: flag = prime_or_not(num) # True if num is prime
            else: flag = num in prime_set 
            if not flag: continue # if num is not prime, then move on to the next set

            for l in range(0,k+1):

                num = int(str(primes[i])+str(primes[l]))
                if num > primes[-1]: flag = prime_or_not(num) 
                else: flag = num in prime_set 
                if not flag: continue 
            
                num = int(str(primes[j])+str(primes[l]))
                if num > primes[-1]: flag = prime_or_not(num) # True if num is prime
                else: flag = num in prime_set 
                if not flag: continue # if num is not prime, then move on to the next set
        
                num = int(str(primes[k])+str(primes[l]))
                if num > primes[-1]: flag = prime_or_not(num) 
                else: flag = num in prime_set 
                if not flag: continue 
            
                num = int(str(primes[l])+str(primes[i]))
                if num > primes[-1]: flag = prime_or_not(num) # True if num is prime
                else: flag = num in prime_set 
                if not flag: continue # if num is not prime, then move on to the next set

                num = int(str(primes[l])+str(primes[j]))
                if num > primes[-1]: flag = prime_or_not(num) 
                else: flag = num in prime_set 
                if not flag: continue 
            
                num = int(str(primes[l])+str(primes[k]))
                if num > primes[-1]: flag = prime_or_not(num) # True if num is prime
                else: flag = num in prime_set 
                if not flag: continue # if num is not prime, then move on to the next set

                for m in range(0,l+1):

                    num = int(str(primes[i])+str(primes[m]))
                    if num > primes[-1]: flag = prime_or_not(num) 
                    else: flag = num in prime_set 
                    if not flag: continue 
                
                    num = int(str(primes[j])+str(primes[m]))
                    if num > primes[-1]: flag = prime_or_not(num) # True if num is prime
                    else: flag = num in prime_set 
                    if not flag: continue # if num is not prime, then move on to the next set

                    num = int(str(primes[k])+str(primes[m]))
                    if num > primes[-1]: flag = prime_or_not(num) 
                    else: flag = num in prime_set 
                    if not flag: continue 
                
                    num = int(str(primes[l])+str(primes[m]))
                    if num > primes[-1]: flag = prime_or_not(num) # True if num is prime
                    else: flag = num in prime_set 
                    if not flag: continue # if num is not prime, then move on to the next set

                    num = int(str(primes[m])+str(primes[i]))
                    if num > primes[-1]: flag = prime_or_not(num) 
                    else: flag = num in prime_set 
                    if not flag: continue 
                
                    num = int(str(primes[m])+str(primes[j]))
                    if num > primes[-1]: flag = prime_or_not(num) # True if num is prime
                    else: flag = num in prime_set 
                    if not flag: continue # if num is not prime, then move on to the next set

                    num = int(str(primes[m])+str(primes[k]))
                    if num > primes[-1]: flag = prime_or_not(num) 
                    else: flag = num in prime_set 
                    if not flag: continue 
                
                    num = int(str(primes[m])+str(primes[l]))
                    if num > primes[-1]: flag = prime_or_not(num) # True if num is prime
                    else: flag = num in prime_set 
                    if not flag: continue # if num is not prime, then move on to the next set

                    s = primes[i] + primes[j] + primes[k] + primes[l] + primes[m]
                    print(f"i:{primes[i]}\tj:{primes[j]}\tk:{primes[k]}\tl:{primes[l]}\tm:{primes[m]}\tsum:{s}")

"""max_prime = 1000000
primes = [2]
for i in range(3,max_prime,2):
    prime = True
    for p in primes:
        if i % p == 0: # if i is divisible by a prime, then it is composite
            prime = False
            break
    if prime:
        # print(i)
        primes.append(i)
with open('primes.txt','w') as f:
    f.write('\n'.join(map(str,primes)))"""
